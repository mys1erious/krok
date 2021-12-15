using System;
using System.Windows;

namespace Ind5.Figures
{
    public class Ellipse : Figure
    {
        public Point Origin { get; }
        public double Width { get; }
        public double Height { get; }
        public double WRadius => Width / 2;
        public double HRadius => Height / 2;

        public Ellipse(Point origin, double width, double height)
        {
            Origin = origin;
            Width = width;
            Height = height;
        }

        public override double Perimeter =>
            Math.PI *
            (3 * (WRadius + HRadius) - Math.Sqrt((3 * WRadius + HRadius) * (WRadius + 3 * HRadius)));

        public override double Area => Math.PI * WRadius * HRadius;

        public override string ToString()
        {
            return $"Type - {Name}\n" +
                   $"Origin - ({Origin})\n" +
                   $"Width - {Width}; Height - {Height}\n" +
                   $"{Utils.ToStringPerimeterAreaTemplate(Perimeter, Area)}";
        }
    }
}