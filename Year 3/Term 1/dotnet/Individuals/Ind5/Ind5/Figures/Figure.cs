
namespace Ind5.Figures
{
    public abstract class Figure
    {
        public string Name => GetType().Name;

        public abstract double Perimeter { get; }
        public abstract double Area { get; }
    }
}