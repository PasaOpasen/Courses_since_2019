using System;
using МатКлассы;
using Complex = МатКлассы.Number.Complex;


namespace TestMyFirstNuget
{
    class Program
    {
        static void Main(string[] args)
        {
            var x = new Complex(1, -2);
            var y = Complex.Cos(x);
            (Complex.Sh(x) + y).Show();
        }
    }
}
