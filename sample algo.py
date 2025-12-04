from kivy.lang import Builder
from kivy_garden.mapview import MapView, MapMarker, MapLayer
from kivy.graphics import Color, Line
from kivy.metrics import dp
from kivymd.app import MDApp

# ------------------------------
# Buildings and intersections
# ------------------------------
VALID_ROOMS = {
    "Ramon Magsaysay": (16.937715315657673, 121.76392437370077),
    "CCSICT Building": (16.938197528772875, 121.764063538908),
    "CBM Building": (16.936043364524572, 121.76446658242533),
    "CED Building": (16.937139129220466, 121.76490974482596),
    "SAS Building": (16.93736905890547, 121.76374652183607),
}

INTERSECTIONS = {
    "Int1_guardpost": (16.935905, 121.764017),
    "Int2_administrationB": (16.936217, 121.764092),
    "Int3_inside_building_left": (16.936343, 121.763921),
    "int4_volly_court": (16.936759, 121.764020),
    "Int5_left_road": (16.936779, 121.763883),
    "int6_left_road_to_chapel": (16.936138, 121.763760),
    "int6_front_sas": (16.937271, 121.763996),
    "Int7_front_magsaysay": (16.937844, 121.764130),
    "Int8_front_ccsict_near_gym": (16.938324, 121.764229),
    "Int9_front_poly_room": (16.938213, 121.764876),
    "Int10_front_educ_faculty": (16.937747, 121.764766),
    "Int11_front_cbm": (16.937077, 121.764618),
    "Int12_front_educ_elem": (16.936674, 121.764519),
    "Int13_basketball_court": (16.936697, 121.764414),
    "Int14_inside_building_right": (16.936220, 121.764259),
    "Int15_front_cbm_building": (16.936017, 121.764347),
    "front_of_ccscit_midman": (16.938095, 121.764178),
    "front_of_magsaysay_midman": (16.937580, 121.764060),
}

# All nodes
NODES = {**VALID_ROOMS, **INTERSECTIONS}

# ------------------------------
# Graph distances (simplified)
# ------------------------------
# ------------------------------
GRAPH = {
    "Int1_guardpost": {
        "Int2_administrationB": 36,
        "int6_left_road_to_chapel": 38,
        "Int15_front_cbm_building": 38

    },
    "Int2_administrationB": {
        "Int1_guardpost": 36,
        "Int3_inside_building_left": 23,
        "Int14_inside_building_right": 19
    },
    "Int3_inside_building_left": {
        "Int2_administrationB": 23,
        "int4_volly_court": 47,

    },
    "Int14_inside_building_right": {
        "Int2_administrationB": 19,
        "Int13_basketball_court": 55
    },
    "int4_volly_court": {
        "Int3_inside_building_left": 47,
        "Int5_left_road": 18
    },
    "Int5_left_road": {
        "int4_volly_court": 18,
        "int6_left_road_to_chapel": 72,
        "int6_front_sas": 56
    },
    "int6_left_road_to_chapel": {
        "Int1_guardpost": 38,
        "Int5_left_road": 72
    },
    "int6_front_sas": {
        "Int5_left_road": 56,
        "Int11_front_cbm": 73,
        "front_of_magsaysay_midman": 35,
        "SAS Building": 6,
    },
    "SAS Building": {
        "int6_front_sas": 6
    },
    "front_of_magsaysay_midman": {
        "Int7_front_magsaysay": 33,
        "int6_front_sas": 35,
        "Ramon Magsaysay": 12
    },
    "Ramon Magsaysay": {
        "front_of_magsaysay_midman": 12
    },
    "Int7_front_magsaysay": {
        "front_of_magsaysay_midman": 33,
        "front_of_ccscit_midman": 29,
        "Int10_front_educ_faculty": 70
    },
    "front_of_ccscit_midman": {
        "Int7_front_magsaysay": 33,
        "Int8_front_ccsict_near_gym": 26,
        "CCSICT Building": 9
    },
    "CCSICT Building": {
        "front_of_ccscit_midman": 9
    },
    "Int8_front_ccsict_near_gym": {
        "front_of_ccscit_midman": 26,
        "Int9_front_poly_room": 74
    },
    "Int9_front_poly_room": {
        "Int8_front_ccsict_near_gym": 74,
        "Int10_front_educ_faculty": 53
    },
    "Int10_front_educ_faculty": {
        "Int9_front_poly_room": 53,
        "Int11_front_cbm": 76,
        "Int7_front_magsaysay": 70
    },
    "Int11_front_cbm": {
        "Int10_front_educ_faculty": 76,
        "CED Building": 9,
        "int6_front_sas": 73,
        "Int12_front_educ_elem": 46,
    },
    "CED Building": {
        "Int11_front_cbm": 9
    },
    "Int12_front_educ_elem": {
        "Int11_front_cbm": 46,
        "Int13_basketball_court": 15,
        "Int15_front_cbm_building": 75
    },
    "Int13_basketball_court": {
        "Int12_front_educ_elem": 15,
        "Int14_inside_building_right": 55
    },
    "Int15_front_cbm_building": {
        "Int12_front_educ_elem": 75,
        "Int1_guardpost": 38,
        "CBM Building": 7
    },
    "CBM Building": {
        "Int15_front_cbm_building": 7
    }

}
# Graph distances (fixed names + symmetric)
# ------------------------------


# ------------------------------
# Dijkstra algorithm
# ------------------------------
def dijkstra(graph, start, end):
    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)
        if dist[current] == float("inf"):
            break
        for neighbor, cost in graph[current].items():
            alt = dist[current] + cost
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current

    path = []
    node = end
    while node:
        path.insert(0, node)
        node = prev[node]
    return path

# ------------------------------
# RouteLine layer
# ------------------------------
class RouteLine(MapLayer):
    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points

    def reposition(self):
        self.canvas.clear()
        mapview = self.parent
        if not mapview:
            return
        with self.canvas:
            Color(1, 0, 0, 1)
            pts = []
            for node in self.points:
                lat, lon = NODES[node]
                x, y = mapview.get_window_xy_from(lat, lon, mapview.zoom)
                pts.extend([x, y])
            if len(pts) >= 4:
                Line(points=pts, width=dp(3))

# ------------------------------
# KV Layout
# ------------------------------
KV = """
MDScreen:

    MapView:
        id: mapview
        lat: 16.9377
        lon: 121.7641
        zoom: 18
        on_zoom:
            if self.zoom > 18: self.zoom = 18
            if self.zoom < 18: self.zoom = 18

    MDRaisedButton:
        text: "Route: Ramon Magsaysay → CBM"
        pos_hint: {"x":0.02, "y":0.02}
        on_release: app.build_route("Int2_administrationB", "CED Building")
"""

# ------------------------------
# Main App
# ------------------------------
class MainApp(MDApp):
    def build(self):
        root = Builder.load_string(KV)
        self.mapview = root.ids.mapview

        # Add markers for all buildings
        for name, (lat, lon) in VALID_ROOMS.items():
            marker1 = MapMarker(lat=lat, lon=lon, source="marker.png")
            marker1.size = (dp(32), dp(32))  # set width and height
            marker1.size_hint = (None, None)
            self.mapview.add_widget(marker1)


        # Add markers for intersections (different color)
        for name, (lat, lon) in INTERSECTIONS.items():
            marker = MapMarker(lat=lat, lon=lon, source="marker_blue.png")
            marker.size = (dp(32), dp(32))  # set width and height
            marker.size_hint = (None, None)  # disable automatic scaling
            self.mapview.add_widget(marker)

        return root

    def build_route(self, start, end):
        # Remove old routes
        for layer in list(self.mapview.children):
            if isinstance(layer, RouteLine):
                self.mapview.remove_widget(layer)

        path = dijkstra(GRAPH, start, end)
        print("PATH:", path)
        route = RouteLine(path)
        self.mapview.add_widget(route)

MainApp().run()
