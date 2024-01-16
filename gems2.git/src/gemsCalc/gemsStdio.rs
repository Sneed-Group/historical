pub fn getCLIInput() -> String {
    let mut input = String::new();
    let b1 = std::io::stdin().read_line(&mut input).unwrap();
    return input;
}