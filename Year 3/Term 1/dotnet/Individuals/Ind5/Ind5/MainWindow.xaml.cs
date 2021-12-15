using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Windows;
using Ind5.Figures;

namespace Ind5
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    
    public partial class MainWindow
    {
        private string _fileName;

        private List<Figure> _figuresList;

        public MainWindow()
        {
            InitializeComponent();
        }
        
        private void ChooseFile_Click(object sender, RoutedEventArgs e)
        {
            // Create OpenFileDialog 
            Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog
            {
                // Set filter for file extension
                DefaultExt = ".txt",
                Filter = "Text files (*.txt)|*.txt"
            };

            // Display OpenFileDialog by calling ShowDialog method 
            bool? result = dlg.ShowDialog();
            
            // Get the selected file name
            if (result == true)
            {
                _fileName = dlg.FileName;
                GetFiguresFromFile();
            }
        }

        private void GetFiguresFromFile()
        {
            _figuresList = new List<Figure>();
            var figuresSource = new ObservableCollection<Figure>();

            var file = File.ReadAllLines(_fileName);
            int numOfFigures = int.Parse(file[0]);

            for (var i = 1; i <= numOfFigures; i++)
            {
                string[] lineArr = file[i].Split(' ');
                AddFigureToFiguresList(lineArr);
                figuresSource.Add(_figuresList[i-1]);
            }
            
            FiguresComboBox.ItemsSource = figuresSource;
        }

        private void AddFigureToFiguresList(string[] lineArr)
        {
            string figureName = lineArr[0];
            
            bool polygon = (figureName == "triangle" || figureName == "rectangle" ||
                            figureName == "square" || figureName == "rhombus");

            Figure figure = default(Figure);
            if (polygon)
            {
                Point[] points = Utils.PolygonPointsBuilder(lineArr);
                switch (figureName)
                {
                    case "triangle":
                        figure = new Triangle(points);
                        break;
                    case "rectangle":
                        figure = new Rectangle(points);
                        break;
                    case "square":
                        figure = new Square(points);
                        break;
                    case "rhombus":
                        figure = new Rhombus(points);
                        break;
                }
            }
            else
            {
                (Point origin, double w, double h) = Utils.EllipseBuilder(lineArr);
                switch (figureName)
                {
                    case "ellipse":
                        figure = new Ellipse(origin, w, h);
                        break;
                    case "circle":
                        figure = new Circle(origin, w);
                        break;
                }
            }
            _figuresList.Add(figure);
        }

        private void CurrentFigure_SelectionChanged(object sender, RoutedEventArgs e)
        {
            FigureInfoLabel.Content = FiguresComboBox.SelectedItem.ToString();
        }

        private void DrawButton_Click(object sender, RoutedEventArgs e)
        {
            Graph graphWin = new Graph((Figure)FiguresComboBox.SelectedItem);
            graphWin.Show();
        }
    }
}
