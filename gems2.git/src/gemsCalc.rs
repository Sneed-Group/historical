mod gemsStdio;

pub fn calc() {
    println!("Modifier (+,-,*,/)>");
    let modifier = gemsStdio::getCLIInput();
    let number1 = gemsStdio::getCLIInput();
    let number2 = gemsStdio::getCLIInput();
    let num1: i32 = number1.parse().unwrap();
    let num2: i32 = number2.parse().unwrap();
    if modifier == "+" {
        println!("{} + {} = {}", num1, num2, num1+num2);
    } else if modifier == "-" {
        println!("{} - {} = {}", num1, num2, num1-num2);
    } else if modifier == "+" {
        println!("{} * {} = {}", num1, num2, num1*num2);
    } else if modifier == "/" {
        println!("{} / {} = {}", num1, num2, num1/num2);
    } else {
        println!("Invalid statement! (Incorrect modifier?)");
    }
}