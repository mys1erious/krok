using System;
using System.Linq;
using System.Windows;

namespace Ind5.Figures
{
    public abstract class Polygon : Figure
    {
        public Point[] Points { get; set; }
        public double[] Sides { get; set; }

        public override double Perimeter => Sides.Sum();

        public override double Area
        {
            get
            {
                double area = 0;
                for (int i = 0; i < Points.Length-1; i++)
                {
                    area += (Points[i + 1].X - Points[i].X) * (Points[i + 1].Y + Points[i].Y) / 2;
                }
                area += (Points[0].X - Points[Points.Length-1].X) * (Points[0].Y + Points[Points.Length-1].Y) / 2;

                return Math.Abs(area);
            }
        }

        public override string ToString()
        {
            return $"Type - {Name}\n" +
                   $"{Utils.ToStringFigureTemplate(Points, Sides)}" +
                   $"{Utils.ToStringPerimeterAreaTemplate(Perimeter, Area)}";
        }
    }
    
}