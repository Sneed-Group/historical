
#include "RevVM.hpp"
#include "RevLAPI.hpp"
#include "RevLINT.hpp"

#pragma region RevVM Defines 
#define rev_setobj(rL, a, b) *(a) = *(b)
#define rev_setobjs2s setobj
#define rev_setobj2s setobj
#define rev_setbvalue(obj, x) { r_TValue *i_o=(obj); i_o->value.b=(x); i_o->tt=R_LUA_TBOOLEAN; }
#define rev_setnilvalue(obj) ((obj)->tt=R_LUA_TNIL)
#define rev_sethvalue { TValue *i_o=(obj); i_o->value.gc=cast(GCObject *, (x)); i_o->tt=R_LUA_TTABLE; }
#define rev_vmtry(x) { __try{x;} __except(rev_luaV_vmcatch(GetExceptionINformation()){})}

#define runtime_check(L, c)	{ if (!(c)) break; }
#define RA(i)	(base+GETARG_A(i))
/* to be used after possible stack reallocation */
#define RB(i)	check_exp(getBMode(GET_OPCODE(i)) == OpArgR, base+GETARG_B(i))
#define RC(i)	check_exp(getCMode(GET_OPCODE(i)) == OpArgR, base+GETARG_C(i))
#define RKB(i)	check_exp(getBMode(GET_OPCODE(i)) == OpArgK, \
	ISK(GETARG_B(i)) ? k+INDEXK(GETARG_B(i)) : base+GETARG_B(i))
#define RKC(i)	check_exp(getCMode(GET_OPCODE(i)) == OpArgK, \
	ISK(GETARG_C(i)) ? k+INDEXK(GETARG_C(i)) : base+GETARG_C(i))
#define KBx(i)	check_exp(getBMode(GET_OPCODE(i)) == OpArgK, k+GETARG_Bx(i))
#define dojump(L,pc,i)	{(pc) += (i); luai_threadyield(L);}
#pragma endregion

typedef TValue r_TValue;

int rev_luaV_vmcatch()
{
	printf("[!] An error occured");
	return 69;
}

r_Proto* rev_luaV_specproto(lua_State *L, Proto* Specification)
{
	r_Proto* rp = rev_luaF_newproto((int)L);
	rp->is_vararg = Specification->is_vararg;
	rp->maxstacksize = Specification->maxstacksize;
	rp->numparams = Specification->numparams;
	return rp;
}

void rev_luaV_execute(lua_State *L, int nexeccalls)
{
	LClosure *cl;
	StkId base;
	TValue *k;
	const Instruction *pc;
reentry:
	pc = L->savedpc;
	cl = (LClosure*)L->ci->func->value.gc;
	base = L->base;
	k = cl->p->k;
	for (;;) {
		const Instruction i = *pc++;
		StkId ra;
		ra = RA(i);
		switch (GET_OPCODE(i)) {
			case OP_MOVE: {
				rev_setobjs2s(L, ra, RB(i));
				continue;
			}
			case OP_LOADK: {
				rev_setobj2s(L, ra, KBx(i));
				continue;
			}
			case OP_LOADBOOL: {
				rev_setbvalue(ra, GETARG_B(i));
				if (GETARG_C(i)) pc++;  /* skip next instruction (if C) */
				continue;
			}
			case OP_LOADNIL: {
				TValue *rb = RB(i);
				do {
					rev_setnilvalue(rb--);
				} while (rb >= ra);
				continue;
			}
			case OP_GETUPVAL: {
				int b = GETARG_B(i);
				rev_setobj2s(L, ra, cl->upvals[b]->v);
				continue;
			}
		}
	}
}
