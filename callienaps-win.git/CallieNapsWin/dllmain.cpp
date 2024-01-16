#include "pch.h"
// dllmain.cpp : Defines the entry point for the DLL application.

#include "../proto.h"
#include "../Bypass/bypass.h"

using namespace std;

lua_State* L;

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }

    return TRUE;
}

int fakeLClosureFunc(lua_State* L) {
    Bypass();
    printf("Doing LClousure Bypass");
    bool LClosure = true;
    luaL_dostring(L, "_G.LClosure = true; LClosure = true; ");
    Restore();
    return 0;
}

int loadstrFunc(lua_State* L) {
    Bypass();
    printf("Do loadstring.");
    const char* script = lua_tostring(L, -1);
    luaL_dostring(L, script);
    fakeLClosureFunc(L);
    Restore();
    return 0;
}

int luaopen_loadstr(lua_State* L) {
    Bypass();
    lua_register(L, "loadstring", loadstrFunc);
    Restore();
    return 0;
}

int luaopen_fakeclosure(lua_State* L) {
    Bypass();
    lua_register(L, "fakeLClosure", fakeLClosureFunc);
    //Restore();
    return 0;
}
int api_runScript(char* code) {
    luaL_dostring(L, code);
    return 0;
}
int main() {
    printf("bypassing...");
    Bypass();
    printf("loading lua...");
    printf("loaded lua, now loading loadstring...");
    L = luaL_newstate();
    luaopen_loadstr(L);
    printf("loading fake closure function...");
    luaopen_fakeclosure(L);
    printf("loading custom functions and ui");
    luaL_openlibs(L);
    luaL_dofile(L, "customluafunc.lua");
    luaL_dofile(L, "gui.lua");
    printf("restoring from bypass...");
    Restore();
}

