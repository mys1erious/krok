using System;
using System.Linq;
using System.Windows;

namespace Ind5.Figures
{
    public class Rectangle : Polygon
    {
        public Rectangle(Point[] points)
        {
            double xMin = points.Min(p => p.X);
            double xMax = points.Max(p => p.X);
            
            double yMin = points.Min(p => p.Y);
            double yMax = points.Max(p => p.Y);

            Points = new []
            {
                new Point(xMin, yMax),
                new Point(xMax, yMax),
                new Point(xMax, yMin),
                new Point(xMin, yMin)
            };
            Sides = new []
            {
                Utils.GetSide(Points[0], Points[1]),
                Utils.GetSide(Points[1], Points[2]),
                Utils.GetSide(Points[2], Points[3]),
                Utils.GetSide(Points[0], Points[3])
            };
        }
    }
}