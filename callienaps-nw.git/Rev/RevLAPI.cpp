
#include "RevLAPI.hpp"

void rev_lua_settop(int rL, signed int idx)
{
	if (idx < 0)
	{
		*(int*)(rL + 16) += 16 * idx + 16;
	}
	else
	{
		int i;
		for (i = 16 * idx; *(int*)(rL + 16) < (unsigned int)(i + *(int*)(rL + 28)); *(int*)(rL + 16) += 16)
			*(int*)(*(int*)(rL + 16) + 8) = 0;
		*(int*)(rL + 16) = i + *(int*)(rL + 28);
	}
}

void rev_lua_pushlightuserdata(int rL, void * ud)
{
	TValue* upv = (TValue*)(*(int*)(rL + 16));
	upv->tt = R_LUA_TLIGHTUSERDATA;
	upv->value.p = ud;
	*(int*)(rL + 16) += 16;
}
