# v1
v1: an interpreter for asm instructions found in the apple silicon (m1) processor in C++.

## how to compile (testing binary)

```
make -j8 $(g++ -std=c++11 v1.cpp -o m1 -fpermissive -ferror-limit=500 -Wc++11-extensions) # replace 8 in -j8 with your cores/threads you wish to use. 
```

## how to compile (library for app developers)

```
make -j8 $(g++ -std=c++11 v1.so -o m1 -fpermissive -ferror-limit=500 -Wc++11-extensions) # note the so file extension. this makes it a library.
```

## what does it do?

it simulates asm instrucitons for apple silicon on an x86_64 mac or any other processor that supports GNU coreutils and C++. (really meant for macos though)

## can it be used for hackintoshing?

probably not, this is intended for developers to make their apps backwards compatible after apple discontinues universial binaries and intel compiling, as it will take me awhile to finish this project (if ever.) however, if one could pull that off, that would be nice! (perhaps with a bootloader that's actually a small linux distro?)

## how to port your app:

* get your asm from your binary.
*  trim the fat and fix bugs. (i.e. remove unsupported calls, test, repeat, etc.)
*  once you have a working version, you can start porting to our instruction set! it is very similar to regular arm64 asm.
  * compile the c++ code as a library
  * write a c++ program to interpret your ASM as seperate C++ functions (i.e. instead of ASM functions), use the "executeASM" function to execute a line of ASM.
  * see if your code works, if so, test and (hopefully) release. if not, try some debugging steps, such as contributing to the project and updating my dumb code to be better or adding your own lines of code to your c++ to make things work (you can do that.)
    * keep in mind some things are slightly different in this arm64 implementation, and some things are even esoteric.
