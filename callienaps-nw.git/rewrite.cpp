#ifndef __LUA_INC_H__
#define __LUA_INC_H__

#include "Bypass/bypass.h"
#include <iostream>
#include <string>
#include <fstream>
#include "General.h"
#include <cstdio>

extern "C" {
#include <stdio.h>
#include <unistd.h>
}

using namespace std;

#pragma region RevVM Defines
#define rev_setobj(rL, a, b) *(a) = *(b)
#define rev_setobjs2s setobj
#define rev_setobj2s setobj
#define rev_setnilvalue(obj) ((obj)->tt=R_LUA_TNIL)
#define rev_vmtry(x) { __try{x;} __except(rev_luaV_vmcatch(GetExceptionINformation()){})}

#define runtime_check(L, c)    { if (!(c)) break; }
#define RA(i)    (base+GETARG_A(i))
/* to be used after possible stack reallocation */
#define RB(i)    check_exp(getBMode(GET_OPCODE(i)) == OpArgR, base+GETARG_B(i))
#define RC(i)    check_exp(getCMode(GET_OPCODE(i)) == OpArgR, base+GETARG_C(i))
#define RKB(i)    check_exp(getBMode(GET_OPCODE(i)) == OpArgK, \
    ISK(GETARG_B(i)) ? k+INDEXK(GETARG_B(i)) : base+GETARG_B(i))
#define RKC(i)    check_exp(getCMode(GET_OPCODE(i)) == OpArgK, \
    ISK(GETARG_C(i)) ? k+INDEXK(GETARG_C(i)) : base+GETARG_C(i))
#define KBx(i)    check_exp(getBMode(GET_OPCODE(i)) == OpArgK, k+GETARG_Bx(i))
#define dojump(L,pc,i)    {(pc) += (i); luai_threadyield(L);}
#pragma endregion


int rev_luaV_vmcatch()
{
    printf("[!] An error occured");
    return 69;
}


int rev_luaV_execute(lua_State *L, int nexeccalls)
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
                if (GETARG_C(i)) pc++;  /* skip next instruction (if C) */
                continue;
            }
            case OP_LOADNIL: {
                continue;
            }
            case OP_GETUPVAL: {
                int b = GETARG_B(i);
                rev_setobj2s(L, ra, cl->upvals[b]->v);
                continue;
            }
        }
    }
    return 0;
}


int fakeLClosureFunc(lua_State *L) {
    Bypass();
    printf("Doing LClousure Bypass");
    bool LClosure = true;
    luaL_dostring(L, "_G.LClosure = true; LClosure = true; ");
    Restore();
    return 0;
}

int loadstrFunc(lua_State *L) {
    Bypass();
    printf("Do loadstring.");
    const char* script = lua_tostring(L, -1);
    int skid = luaL_dostring(L, script);
    rev_luaV_execute(L, skid);
    fakeLClosureFunc(L);
    Restore();
    return 0;
}

int luaopen_loadstr(lua_State *L){
    Bypass();
    lua_register(L,"loadstring",loadstrFunc);
    Restore();
    return 0;
}

int luaopen_fakeclosure(lua_State *L){
    Bypass();
    lua_register(L,"fakeLClosure",fakeLClosureFunc);
    Restore();
    return 0;
}

auto luaustring_address = 0x01337610;
auto x(auto toReturn) {
    return toReturn; 
} 

using Luaustring_def = int; 
Luaustring_def Luaustring = (Luaustring_def)(x(luaustring_address));

int main() {
    printf("bypassing...");
    Bypass();
    printf("loading lua...");
    lua_State *Lold;
    Lold = luaL_newstate();
    lua_State *L = loadNewState(Lold);
    lua_newthread(L);
    printf("loaded lua, now loading loadstring...");
    luaopen_loadstr(L);
    int hello = luaL_dostring(L, "print('Hello, world! If you see this, it works!')");
    rev_luaV_execute(L, hello);
    printf("loading fake closure function...");
    luaopen_fakeclosure(L);
    printf("loading custom functions and ui");
    loadUI(L);
    printf("restoring from bypass...");
    Restore();
}

#endif // __LUA_INC_H__
