using System;
using System.Windows;

namespace Ind5.Figures
{
    public static class Utils
    {
        public static double GetSide(Point p1, Point p2)
        {
            return Math.Sqrt(Math.Pow(p1.X - p2.X, 2) + Math.Pow(p1.Y - p2.Y, 2));
        }
        
        public static string ToStringFigureTemplate(Point[] points, double[] sides)
        {
            string pointsStr = "";
            for (var p = 0; p < points.Length; p++)
            {
                pointsStr += $"p{p} = ({points[p]}); ";
            }
                
            string sidesStr = "";
            for (var s = 0; s < sides.Length; s++)
            {
                sidesStr += $"s{s} = {sides[s]:0.00}; ";
            }

            string result = $"{pointsStr}\n" +
                            $"{sidesStr}\n";
            return result;
        }
        
        public static string ToStringPerimeterAreaTemplate(double perimeter, double area)
        {
            string result = $"Perimeter = {perimeter:0.00}\n" +
                            $"area = {area:0.00}";
            return result;
        }

        public static Point[] PolygonPointsBuilder(string[] lineArr)
        {
            Point[] points;
            int numOfPoints = 0;
            int ind = 0;
            
            switch (lineArr[0])
            {
                case "triangle":
                    numOfPoints = 3;
                    break;
                case "rectangle":
                case "square":
                case "rhombus":
                    numOfPoints = 4;
                    break;
                case "circle":
                case "ellipse":
                    numOfPoints = 1;
                    break;
            }
            
            points = new Point[numOfPoints];
            for (int p = 1; p < lineArr.Length-1; p+=2)
            {
                points[ind] = new Point(
                    double.Parse(lineArr[p], System.Globalization.CultureInfo.InvariantCulture),
                    double.Parse(lineArr[p+1], System.Globalization.CultureInfo.InvariantCulture));
                ind++;
            }

            return points;
        }

        public static (Point, double, double) EllipseBuilder(string[] lineArr)
        {
            Point origin = new Point(
                double.Parse(lineArr[1], System.Globalization.CultureInfo.InvariantCulture),
                double.Parse(lineArr[2], System.Globalization.CultureInfo.InvariantCulture)
            );
            double w = double.Parse(lineArr[3], System.Globalization.CultureInfo.InvariantCulture);
            try
            {
                double h = double.Parse(lineArr[4], System.Globalization.CultureInfo.InvariantCulture);
                return (origin, w, h);
            }
            catch
            {
                // ignored
            }
            
            return (origin, w, w);
        }
    }
}