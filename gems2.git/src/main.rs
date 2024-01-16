#![no_std] // don't link the Rust standard library
#![no_main] // disable all Rust-level entry points

mod stdgem;
use stdgem::print;
use core::panic::PanicInfo;
//static GEMS2: &[u8] = b"WELCOME TO GEMS 2! =)";
#[no_mangle] // don't mangle the name of this function
pub extern "C" fn _start() -> ! {
    print("WELCOME TO GEMS 2! =)");
    loop {}
}

/// This function is called on panic.
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
