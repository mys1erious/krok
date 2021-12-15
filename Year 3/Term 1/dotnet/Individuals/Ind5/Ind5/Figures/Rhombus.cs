using System;
using System.Linq;
using System.Windows;

namespace Ind5.Figures
{
    public class Rhombus : Polygon
    {
        public Rhombus(Point[] points)
        {
            double xMin = points.Min(p => p.X);
            double xMax = points.Max(p => p.X);
            double xMid = (xMax + xMin) / 2;
            
            double yMin = points.Min(p => p.Y);
            double yMax = points.Max(p => p.Y);
            double yMid = (yMax + yMin) / 2;
            
            Points = new []
            {
                new Point(xMin, yMid),
                new Point(xMid, yMax),
                new Point(xMax, yMid),
                new Point(xMid, yMin)
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