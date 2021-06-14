import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import math

rospy.init_node('draw_frustum')
pub_line_min_dist = rospy.Publisher('~draw_frustum', Marker, queue_size=1)
rospy.loginfo('Starting to draw camera frustum')


def get_camera_topics():
    all_topics = rospy.get_published_topics()
    # print(topics[1])
    camera_topics = all_topics

    return camera_topics


def get_parameters():
    return 0


def calculate_frustum(w, h, f_x, f_y, frame_id):
    marker = Marker()

    marker.type = marker.LINE_LIST
    marker.action = marker.ADD
    marker.header.frame_id = frame_id
    # marker scale
    marker.scale.x = 0.01

    # marker color
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 1.0
    marker.color.b = 0.0

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

    Z_near = 2
    Z_far = 5
    fov_x = 2 * math.atan2(w, (2 * f_x))
    fov_y = 2 * math.atan2(h, (2 * f_y))

    x_n = (fov_x * 25.4 * Z_near) / f_x
    y_n = (fov_y * 25.4 * Z_near) / f_y

    x_f = (fov_x * 25.4 * Z_far) / f_x
    y_f = (fov_y * 25.4 * Z_far) / f_y

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
    frame_id = "map"
    w = 640
    h = 480
    f_x = 529.74
    f_y = 530.53

    marker = calculate_frustum(w, h, f_x, f_y, frame_id)
    # Publish the Marker
    pub_line_min_dist.publish(marker)

    rospy.sleep(0.5)
