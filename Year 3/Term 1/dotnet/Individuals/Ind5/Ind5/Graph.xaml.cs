using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Shapes;
using Ind5.Figures;
using Ellipse = System.Windows.Shapes.Ellipse;

namespace Ind5
{
    public partial class Graph : Window
    {
        private object FigureToDraw;
        private const double Step = 30;
        private const double UnitSize = 3;
        
        private Brush AxisBrush = Brushes.Black;
        private Brush FigureOuterBrush = Brushes.DarkBlue;
        // private Brush FigureInnerBrush = Brushes.Gray;
        
        public Graph(Figure figure)
        {
            InitializeComponent();
            FigureToDraw = figure;
        }
        
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            const double margin = 10;
            
            double xMin = margin;
            double xMax = CanGraph.Width - margin;
            double xMid = (xMax - xMin) / 2;
            
            double yMin = margin;
            double yMax = CanGraph.Height - margin;
            double yMid = (yMax - yMin) / 2;
            

            // Make the X axis.
            var xAxisGeomGroup = new GeometryGroup();
            xAxisGeomGroup.Children.Add(new LineGeometry(new Point(xMin, yMid), new Point(xMax, yMid)));

            for (double x = xMid; x < xMax; x += Step)
            {
                xAxisGeomGroup.Children.Add(new LineGeometry(
                    new Point(x, yMid - UnitSize),
                    new Point(x, yMid + UnitSize)));
            }
            for (double x = xMid; x > xMin; x -= Step)
            {
                xAxisGeomGroup.Children.Add(new LineGeometry(
                    new Point(x, yMid - UnitSize),
                    new Point(x, yMid + UnitSize)));
            }
            
            var xAxisPath = new Path
            {
                StrokeThickness = 1,
                Stroke = AxisBrush,
                Data = xAxisGeomGroup
            };
            CanGraph.Children.Add(xAxisPath);

            
            // Make the Y axis.
            var yAxisGeomGroup = new GeometryGroup();
            yAxisGeomGroup.Children.Add(new LineGeometry(new Point(xMid, yMin), new Point(xMid, yMax)));
            
            for (double y = yMid; y < yMax; y += Step)
            {
                yAxisGeomGroup.Children.Add(new LineGeometry(
                    new Point(xMid - UnitSize, y),
                    new Point(xMid + UnitSize, y)));
            }
            for (double y = yMid; y > yMin; y -= Step)
            {
                yAxisGeomGroup.Children.Add(new LineGeometry(
                    new Point(xMid - UnitSize, y),
                    new Point(xMid + UnitSize, y)));
            }
            
            var yAxisPath = new Path
            {
                StrokeThickness = 1,
                Stroke = AxisBrush,
                Data = yAxisGeomGroup
            };
            CanGraph.Children.Add(yAxisPath);
            
            
            // Make a figure
            var figureType = FigureToDraw?.GetType();
            
            if (figureType != null)
                switch (figureType.Name)
                {
                    case "Triangle":
                    case "Rectangle":
                    case "Square":
                    case "Rhombus":
                        var polygonPoints = (Point[])GetPropValue(figureType, "Points", FigureToDraw);
                        DrawPolygon(polygonPoints, xMid, yMid);
                        break;
                    case "Circle":
                    case "Ellipse":
                        var origin = (Point)GetPropValue(figureType, "Origin", FigureToDraw);
                        var w = (double)GetPropValue(figureType, "Width", FigureToDraw);
                        var h = (double)GetPropValue(figureType, "Height", FigureToDraw);
                        DrawEllipse(origin, w, h, xMid, yMid);
                        break;
                }
        }
        
        private void DrawEllipse(Point origin, double w, double h, double xMid, double yMid)
        {
            var ellipse = new Ellipse();
            
            w *= Step;
            h *= Step;
            ellipse.Width = w;
            ellipse.Height = h;
            
            Point scaledOrigin = AdjustPoint(xMid, yMid, origin);
            scaledOrigin.X -= w / 2;
            scaledOrigin.Y -= h / 2;
            
            Canvas.SetLeft(ellipse, scaledOrigin.X);
            Canvas.SetTop(ellipse, scaledOrigin.Y);
            
            ellipse.StrokeThickness = 2;
            ellipse.Stroke = FigureOuterBrush;

            CanGraph.Children.Add(ellipse);
        }
        
        private void DrawPolygon(Point[] pointsArr, double xMid, double yMid)
        {
            var polyline = new Polyline();
            PointCollection points = new PointCollection();

            if (pointsArr != null)
            {
                foreach (var p in pointsArr)
                {
                    var scaledPoint = AdjustPoint(xMid, yMid, p);
                    points.Add(scaledPoint);
                }
                points.Add(AdjustPoint(xMid, yMid, pointsArr[0]));
            }

            polyline.StrokeThickness = 2;
            polyline.Stroke = FigureOuterBrush;
            polyline.Points = points;
            
            CanGraph.Children.Add(polyline);
        }
        
        private Point AdjustPoint(double xMid, double yMid, Point p)
        {
            return new Point(xMid + (p.X * Step), yMid - (p.Y * Step));
        }
        
        private object GetPropValue(Type type, string prop, object obj)
        {
            return type.GetProperty($"{prop}")?.GetValue(obj, null);
        }
    }
}
