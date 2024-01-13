from figures import Rectangle, Square, Circle


def read_file(filename):
    figures = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            if len(data) < 2:
                print(f"Invalid data: {line}")
                continue
            figure_type = data[0].strip().lower()
            if figure_type == 'rectangle' and len(data) >= 3:
                width = int(data[1])
                height = int(data[2])
                figures.append(Rectangle(width, height))
            elif figure_type == 'square' and len(data) >= 2:
                side = int(data[1])
                figures.append(Square(side))
            elif figure_type == 'circle' and len(data) >= 2:
                radius = int(data[1])
                figures.append(Circle(radius))
            else:
                print(f"{figure_type} is an unknown figure")
    return figures


def get_perimeters(list_of_figures):
    for fig in list_of_figures:
        print(f"{fig.__class__.__name__} has following perimeter: {fig.calc_perimeter():.2f}")


def get_areas(list_of_figures):
    for fig in list_of_figures:
        print(f"{fig.__class__.__name__} has following area: {fig.calc_area():.2f}")
