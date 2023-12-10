from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# Função para criar um único cruzamento
def create_intersection(x_offset, y_offset):
    # SOUTH, EAST, NORTH, WEST

    # Intersection in
    sim.create_segment((lane_space/2 + x_offset, length+intersection_size/2 + y_offset), (lane_space/2 + x_offset, intersection_size/2 + y_offset))
    sim.create_segment((length+intersection_size/2 + x_offset, -lane_space/2 + y_offset), (intersection_size/2 + x_offset, -lane_space/2 + y_offset))
    sim.create_segment((-lane_space/2 + x_offset, -length-intersection_size/2 + y_offset), (-lane_space/2 + x_offset, -intersection_size/2 + y_offset))
    sim.create_segment((-length-intersection_size/2 + x_offset, lane_space/2 + y_offset), (-intersection_size/2 + x_offset, lane_space/2 + y_offset))
    # Intersection out
    sim.create_segment((-lane_space/2 + x_offset, intersection_size/2 + y_offset), (-lane_space/2 + x_offset, length+intersection_size/2 + y_offset))
    sim.create_segment((intersection_size/2 + x_offset, lane_space/2 + y_offset), (length+intersection_size/2 + x_offset, lane_space/2 + y_offset))
    sim.create_segment((lane_space/2 + x_offset, -intersection_size/2 + y_offset), (lane_space/2 + x_offset, -length-intersection_size/2 + y_offset))
    sim.create_segment((-intersection_size/2 + x_offset, -lane_space/2 + y_offset), (-length-intersection_size/2 + x_offset, -lane_space/2 + y_offset))
    # Straight
    sim.create_segment((lane_space/2 + x_offset, intersection_size/2 + y_offset), (lane_space/2 + x_offset, -intersection_size/2 + y_offset))
    sim.create_segment((intersection_size/2 + x_offset, -lane_space/2 + y_offset), (-intersection_size/2 + x_offset, -lane_space/2 + y_offset))
    sim.create_segment((-lane_space/2 + x_offset, -intersection_size/2 + y_offset), (-lane_space/2 + x_offset, intersection_size/2 + y_offset))
    sim.create_segment((-intersection_size/2 + x_offset, lane_space/2 + y_offset), (intersection_size/2 + x_offset, lane_space/2 + y_offset))
    # Right turn
    sim.create_quadratic_bezier_curve((lane_space/2 + x_offset, intersection_size/2 + y_offset), (lane_space/2 + x_offset, lane_space/2 + y_offset), (intersection_size/2 + x_offset, lane_space/2 + y_offset))
    sim.create_quadratic_bezier_curve((intersection_size/2 + x_offset, -lane_space/2 + y_offset), (lane_space/2 + x_offset, -lane_space/2 + y_offset), (lane_space/2 + x_offset, -intersection_size/2 + y_offset))
    sim.create_quadratic_bezier_curve((-lane_space/2 + x_offset, -intersection_size/2 + y_offset), (-lane_space/2 + x_offset, -lane_space/2 + y_offset), (-intersection_size/2 + x_offset, -lane_space/2 + y_offset))
    sim.create_quadratic_bezier_curve((-intersection_size/2 + x_offset, lane_space/2 + y_offset), (-lane_space/2 + x_offset, lane_space/2 + y_offset), (-lane_space/2 + x_offset, intersection_size/2 + y_offset))
    # Left turn
    sim.create_quadratic_bezier_curve((lane_space/2 + x_offset, intersection_size/2 + y_offset), (lane_space/2 + x_offset, -lane_space/2 + y_offset), (-intersection_size/2 + x_offset, -lane_space/2 + y_offset))
    sim.create_quadratic_bezier_curve((intersection_size/2 + x_offset, -lane_space/2 + y_offset), (-lane_space/2 + x_offset, -lane_space/2 + y_offset), (-lane_space/2 + x_offset, intersection_size/2 + y_offset))
    sim.create_quadratic_bezier_curve((-lane_space/2 + x_offset, -intersection_size/2 + y_offset), (-lane_space/2 + x_offset, lane_space/2 + y_offset), (intersection_size/2 + x_offset, lane_space/2 + y_offset))
    sim.create_quadratic_bezier_curve((-intersection_size/2 + x_offset, lane_space/2 + y_offset), (lane_space/2 + x_offset, lane_space/2 + y_offset), (lane_space/2 + x_offset, -intersection_size/2 + y_offset))

# Criar 4 cruzamentos
create_intersection(0, 0)
create_intersection(length + intersection_size, 0)
create_intersection(0, length + intersection_size)
create_intersection(length + intersection_size, length + intersection_size)

vg1 = VehicleGenerator({
    'vehicles': [
        (1, {'path': [0, 8, 6], 'v': 16.6}),
        (1, {'path': [0, 12, 5], 'v': 16.6})
        ]
    })
sim.add_vehicle_generator(vg1)

vg2 = VehicleGenerator({
    'vehicles': [
        (2, {'path': [1, 9, 7], 'v': 20.0}),
        (2, {'path': [1, 13, 6], 'v': 20.0})
        ]
    })
sim.add_vehicle_generator(vg2)

vg3 = VehicleGenerator({
    'vehicles': [
        (3, {'path': [2, 10, 8], 'v': 25.0}),
        (3, {'path': [2, 14, 7], 'v': 25.0})
        ]
    })
sim.add_vehicle_generator(vg3)

win = Window(sim)
win.run()
win.show()
