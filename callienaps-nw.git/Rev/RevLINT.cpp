#include "RevLINT.hpp"

void rev_luaC_link(int r_lua_State, int o, int tt)
{
	int g = lint_deptr(r_lua_State + 8);	// global_State *g = G(L)
	*(int*)(o) = *(int*)(g + 48);			// o->gch.next = g->rootgc
	*(int*)(g + 48) = o;					// g->rootgc = o
	*(int*)(o + 4) = *(int*)(g + 21) & 3;	// o->gch.marked = luaC_white(g)
	*(int*)(o + 5) = tt;					// o->gch.tt = tt;
}

void* rev_luaM_realloc_(int r_lua_State, int block, int osize, int nsize)
{
	return nullptr;
}

r_Proto* rev_luaF_newproto(int r_lua_State)
{
	r_Proto* f = rev_luaM_new(r_lua_State, r_Proto);
	rev_luaC_link(r_lua_State, (int)f, R_LUA_TPROTO);
	return f;
}