from manim import Scene, Square, VGroup, there_and_back, BLUE, YELLOW, Create, RegularPolygon, RIGHT, Text, UP

class HexagonNeighbors(Scene):
    def construct(self):
        # Create hexagonal grid
        hexagons = VGroup()
        for i in range(7):
            for j in range(7):
                hexagon = RegularPolygon(n=6, color=BLUE, fill_opacity=0.5).scale(0.5)
                hexagon.move_to((i - 3) * RIGHT + (j - 3) * RIGHT * 1.5)
                hexagons.add(hexagon)
        
        # Highlight number of neighbors for center hexagon
        center_hexagon = hexagons[24]  # Assuming center hexagon is at index 24
        center_hexagon.set_color(YELLOW)
        # num_neighbors = len(center_hexagon.get_all_neighbors())
        # num_neighbors_label = Text(f"Number of neighbors: {num_neighbors}").next_to(center_hexagon, UP)
        
        self.play(Create(hexagons), Create(center_hexagon), )
        self.wait()
    