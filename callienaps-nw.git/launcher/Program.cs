using System.Runtime.InteropServices;
using System;

namespace HelloWorldLaunch {
public class HelloWorld
{
	public static void Main(string[] args)
	{
		try {
			[DllImport("callienaps_blue_main.so")]
			static extern int main ();
			main();
			Console.WriteLine("LETS GO! We injected!");
		} catch {
			Console.WriteLine(":( didnt work");
		}
	}
}
}
