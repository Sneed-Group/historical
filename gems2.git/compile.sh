cd ./
cargo clean
#cd ./bootloader-main
#cargo clean
#cd ..
#cargo builder --kernel-manifest ../gemsExp-main/Cargo.toml --kernel-binary ../gemsExp-main/target/debug/GEMS-EXPERIENCE
cargo build --target os-target.json -Zbuild-std
