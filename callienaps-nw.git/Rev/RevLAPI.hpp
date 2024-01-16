#pragma once

#include "RevBase.hpp"

void r_lua_settop(lua_State rL, signed int idx);
void r_lua_pushlightuserdata(lua_State RL, void* ud);
