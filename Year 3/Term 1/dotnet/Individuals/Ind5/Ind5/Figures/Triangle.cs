using System;
using System.Linq;
using System.Windows;

namespace Ind5.Figures
{
    public class Triangle : Polygon
    {
        public Triangle(Point[] points)
        {
            Points = points;
            Sides = new []
            {
                Utils.GetSide(points[1], points[2]),
                Utils.GetSide(points[0], points[2]),
                Utils.GetSide(points[0], points[1])
            };
        }
    }
}