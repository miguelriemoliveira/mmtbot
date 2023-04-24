import numpy
import rospy
from numpy import rad2deg
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from sensor_msgs.msg import CameraInfo, Image
from visualization_msgs.msg import MarkerArray
import random

import math
import image_geometry

rospy.init_node('draw_frustums')
# n=get_camera_topics().shape()
# print(n)
publisher = rospy.Publisher('~draw_frustums', MarkerArray, queue_size=1)
rospy.loginfo('Starting to draw camera frustum')


def get_camera_topics():
    all_topics = rospy.get_published_topics()
    # print(all_topics)
    flat_list = [item for sublist in all_topics for item in sublist]
    filtered_topics = [x for x in flat_list if (
        (x.startswith('/world_camera') and x.endswith('camera_info') and not x.endswith(
            '/ir/camera_info') and not x.endswith('/depth_registered/camera_info') and not x.endswith(
            '/projector/camera_info') and not x.endswith('/sw_registered/camera_info'))) or (
                                   x.startswith('/hand_camera') and x.endswith('camera_info'))]
    print(filtered_topics)
    return filtered_topics


def calculate_frustum(w, h, f_x, f_y, frame_id,color):
    marker = Marker()

    marker.type = marker.LINE_LIST
    marker.action = marker.ADD
    marker.header.frame_id = frame_id
    # marker scale
    marker.scale.x = 0.01

    # marker color
    marker.color.a = 1.0
    marker.color.r = color[0]
    marker.color.g = color[1]
    marker.color.b = color[2]

    # marker orientaiton
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    # marker position
    marker.pose.position.x = 0.0
    marker.pose.position.y = 0.0
    marker.pose.position.z = 0.0

    P1 = Point()
    P2 = Point()
    P3 = Point()
    P4 = Point()
    P5 = Point()
    P6 = Point()
    P7 = Point()
    P8 = Point()

    Z_near = 0.3
    Z_far = 8
    fov_x = 2 * math.atan2(w, (2 * f_x))
    fov_y = 2 * math.atan2(h, (2 * f_y))

    # print(rad2deg(fov_x), rad2deg(fov_y))

    x_n = math.tan(fov_x / 2) * Z_near
    y_n = math.tan(fov_y / 2) * Z_near

    x_f = math.tan(fov_x / 2) * Z_far
    y_f = math.tan(fov_y / 2) * Z_far

    P1.x = -x_n
    P1.y = y_n
    P1.z = Z_near

    P2.x = x_n
    P2.y = y_n
    P2.z = Z_near

    P3.x = x_n
    P3.y = -y_n
    P3.z = Z_near

    P4.x = -x_n
    P4.y = -y_n
    P4.z = Z_near

    P5.x = -x_f
    P5.y = y_f
    P5.z = Z_far

    P6.x = x_f
    P6.y = y_f
    P6.z = Z_far

    P7.x = x_f
    P7.y = -y_f
    P7.z = Z_far

    P8.x = -x_f
    P8.y = -y_f
    P8.z = Z_far

    # marker line points
    marker.points = []

    marker.points.append(P1)
    marker.points.append(P2)

    marker.points.append(P2)
    marker.points.append(P3)

    marker.points.append(P3)
    marker.points.append(P4)

    marker.points.append(P4)
    marker.points.append(P1)

    marker.points.append(P1)
    marker.points.append(P5)
    #
    marker.points.append(P2)
    marker.points.append(P6)

    marker.points.append(P3)
    marker.points.append(P7)

    marker.points.append(P4)
    marker.points.append(P8)

    marker.points.append(P5)
    marker.points.append(P6)

    marker.points.append(P6)
    marker.points.append(P7)

    marker.points.append(P7)
    marker.points.append(P8)

    marker.points.append(P8)
    marker.points.append(P5)
    return marker


while not rospy.is_shutdown():
    # frame_id = "map"
    # w = 640
    # h = 480
    # f_x = 529.74
    # f_y = 530.53
    marker_array = MarkerArray()
    topics = get_camera_topics()
    pinhole_camera_model = image_geometry.PinholeCameraModel()
    n = 0

    colors = numpy.array([[255, 0, 0], [255, 128, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 128, 255], [0, 0, 255],
              [128, 0, 255], [255, 0, 255], [255, 0, 128]])

    # camera_info_topic = "/io/internal_camera/{}/camera_info".format(camera_name)
    for topic in topics:
        camera_info = rospy.wait_for_message(topic, CameraInfo)
        pinhole_camera_model.fromCameraInfo(camera_info)
        f_x = pinhole_camera_model.fx()
        f_y = pinhole_camera_model.fy()
        frame_id = pinhole_camera_model.tfFrame()
        size = pinhole_camera_model.fullResolution()
        # print(f_x,f_y)
        # print(frame_id)
        # print(size)
        w = size[0]
        h = size[1]
        marker_n = calculate_frustum(w, h, f_x, f_y, frame_id, colors[n]/255)
        # print(colors[n])
        marker_n.id = n
        # Publish the Marker
        marker_array.markers.append(marker_n)
        n += 1
        # pub_line_min_dist.publish(marker)

    publisher.publish(marker_array)
    rospy.sleep(1)
