class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        
    def get_picture(self):
        picture = "Too big for picture."
        if self.width < 50 and self.height < 50:
            draw_width = '*' * self.width
            picture = (draw_width + '\n') * self.height
        
        return picture

    def get_amount_inside(self, shape):
        if self.width < shape.width and self.height < shape.height:
            return 0
        width_multiple = int(self.width / shape.width)
        height_multiple = int(self.height / shape.height)

        return width_multiple * height_multiple


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.side(side)