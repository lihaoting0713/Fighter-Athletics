from graphics import *

#text pools
text_ui = None
text_ui1 = None
text_ui2 = None
text_boxing_room = None
text_leg_training_room = None
text_command = None
text_command2 = None
text_command3_final = None
text_final_chanllenge = None
level_ui = None
inventory_ui = None
inventory_items = None
level_multi = 1.0
person_level = 0
#vsisted room and pllayer's actions
visited_room = []
player_action = ["Hey! These are your actions in the game", ""]
#for statistics, player's performance analysis
level_history_room = []
level_history_level = []
#Inventory analysis
inventory = []
inventory_award = 0


# create a noraml person
def person(center, win):
    head = Circle(center,  20)
    head.setFill("white")
    head.draw(win)

    arm1center1 = center.clone()
    arm1center1.move(-35, 40)
    arm1center2 = center.clone()
    arm1center2.move(-60, 90)
    arm1 = Line(arm1center1, arm1center2)
    arm1.setWidth(10)
    arm1.draw(win)

    arm2center1 = center.clone()
    arm2center1.move(35, 40)
    arm2center2 = center.clone()
    arm2center2.move(60, 90)
    arm2 = Line(arm2center1, arm2center2)
    arm2.setWidth(10)
    arm2.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 105)
    leg1center2 = center.clone()
    leg1center2.move(-5, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 105)
    leg2center2 = center.clone()
    leg2center2.move(5, 200)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    return [head, body, arm1, arm2, leg1, leg2]


#create a running person
def running_person(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm1center1 = center.clone()
    arm1center1.move(-35, 40)
    arm1center2 = center.clone()
    arm1center2.move(-60, 90)
    arm1 = Line(arm1center1, arm1center2)
    arm1.setWidth(10)
    arm1.draw(win)

    arm2center1 = center.clone()
    arm2center1.move(35, 40)
    arm2center2 = center.clone()
    arm2center2.move(60, 90)
    arm2 = Line(arm2center1, arm2center2)
    arm2.setWidth(10)
    arm2.draw(win)

    left_leg_center1 = center.clone()
    left_leg_center1.move(-10,100)
    left_leg_center2 = center.clone()
    left_leg_center2.move(-25,150)
    left_leg = Line(left_leg_center1,left_leg_center2)
    left_leg.setWidth(20)
    left_leg.draw(win)

    left_leg1_center1 =center.clone()
    left_leg1_center1.move(-21,145)
    left_leg1_center2 = center.clone()
    left_leg1_center2.move(-60,170)
    left_leg1 = Line(left_leg1_center1,left_leg1_center2)
    left_leg1.setWidth(18)
    left_leg1.draw(win)

    right_leg_center1 = center.clone()
    right_leg_center1.move(10,100)
    right_leg_center2 = center.clone()
    right_leg_center2.move(25,150)
    right_leg = Line(right_leg_center1,right_leg_center2)
    right_leg.setWidth(20)
    right_leg.draw(win)

    right_leg1_center1 = center.clone()
    right_leg1_center1.move(25,143)
    right_leg1_center2 = center.clone()
    right_leg1_center2.move(10,190)
    right_leg1 = Line(right_leg1_center1,right_leg1_center2)
    right_leg1.setWidth(18)
    right_leg1.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)


    return [head, body, arm1, arm2, left_leg, left_leg1, right_leg, right_leg1]

#create a person training arms
def exercise_person(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm_left_center1 = center.clone()
    arm_left_center1.move(-35, 40)
    arm_left_center2 = center.clone()
    arm_left_center2.move(-45, 80)
    arm_left = Line(arm_left_center1, arm_left_center2)
    arm_left.setWidth(10)
    arm_left.draw(win)

    arm_left1_center1 = center.clone()
    arm_left1_center1.move(-48, 82)
    arm_left1_center2 = center.clone()
    arm_left1_center2.move(-55, 50)
    arm_left1 = Line(arm_left1_center1, arm_left1_center2)
    arm_left1.setWidth(10)
    arm_left1.draw(win)

    arm_right_center1 = center.clone()
    arm_right_center1.move(35, 40)
    arm_right_center2 = center.clone()
    arm_right_center2.move(45, 80)
    arm_right = Line(arm_right_center1, arm_right_center2)
    arm_right.setWidth(10)
    arm_right.draw(win)

    arm_right1_center1 = center.clone()
    arm_right1_center1.move(48, 82)
    arm_right1_center2 = center.clone()
    arm_right1_center2.move(55, 50)
    arm_right1 = Line(arm_right1_center1, arm_right1_center2)
    arm_right1.setWidth(10)
    arm_right1.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 105)
    leg1center2 = center.clone()
    leg1center2.move(-5, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 105)
    leg2center2 = center.clone()
    leg2center2.move(5, 200)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)


    return [head, body, leg1, leg2, arm_left, arm_left1, arm_right, arm_right1]


#create a person with injuered arms
def broken_arm_person(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm_left_center1 = center.clone()
    arm_left_center1.move(-35, 40)
    arm_left_center2 = center.clone()
    arm_left_center2.move(-45, 80)
    arm_left = Line(arm_left_center1, arm_left_center2)
    arm_left.setWidth(10)
    arm_left.draw(win)

    arm_right_center1 = center.clone()
    arm_right_center1.move(35, 40)
    arm_right_center2 = center.clone()
    arm_right_center2.move(45, 80)
    arm_right = Line(arm_right_center1, arm_right_center2)
    arm_right.setWidth(10)
    arm_right.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    arm1_left1_2_center1 = center.clone()
    arm1_left1_2_center1.move(-45, 82)
    arm1_left1_2_center2 = center.clone()
    arm1_left1_2_center2.move(-20, 95)
    arm1_left1_2 = Line(arm1_left1_2_center1, arm1_left1_2_center2)
    arm1_left1_2.setWidth(10)
    arm1_left1_2.draw(win)

    arm1_right1_2_center1 = center.clone()
    arm1_right1_2_center1.move(45, 82)
    arm1_right1_2_center2 = center.clone()
    arm1_right1_2_center2.move(25, 106)
    arm1_right1_2 = Line(arm1_right1_2_center1, arm1_right1_2_center2)
    arm1_right1_2.setWidth(10)
    arm1_right1_2.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 105)
    leg1center2 = center.clone()
    leg1center2.move(-5, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 105)
    leg2center2 = center.clone()
    leg2center2.move(5, 200)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    return [head, body, leg1, leg2, arm_right, arm_left, arm1_right1_2, arm1_left1_2]


# create a weight for legs training
def weight(center, win):
    weight_middle_center1 = center.clone()
    weight_middle_center1.move(-110, -8)
    weight_middle_center2 = center.clone()
    weight_middle_center2.move(110, 8)
    weight_middle = Rectangle(weight_middle_center1, weight_middle_center2)
    weight_middle.setFill("silver")
    weight_middle.setOutline("silver")
    weight_middle.draw(win)

    weight_left_center1 = center.clone()
    weight_left_center1.move(-90, 52)
    weight_left_center2 = center.clone()
    weight_left_center2.move(-130, -53)
    weight_left = Oval(weight_left_center1, weight_left_center2)
    weight_left.setFill("black")
    weight_left.draw(win)

    weight_right = weight_left.clone()
    weight_right.move(220, 0)
    weight_right.setFill("black")
    weight_right.draw(win)

    return [weight_middle, weight_left, weight_right]

#create a small weight for arms training
def small_weight(center, win):
    small_weight_middle_center1 = center.clone()
    small_weight_middle_center1.move(-19, -5)
    small_weight_middle_center2 = center.clone()
    small_weight_middle_center2.move(19, 5)
    small_weight_middle = Rectangle(small_weight_middle_center1, small_weight_middle_center2)
    small_weight_middle.setFill("black")
    small_weight_middle.draw(win)

    small_weight_left_center1 = center.clone()
    small_weight_left_center1.move(-29, -15)
    small_weight_left_center2 = center.clone()
    small_weight_left_center2.move(-19, 15)
    small_weight_left = Rectangle(small_weight_left_center1, small_weight_left_center2)
    small_weight_left.setFill("black")
    small_weight_left.draw(win)

    small_weight_right = small_weight_left.clone()
    small_weight_right.move(48, 0)
    small_weight_right.draw(win)

    return [small_weight_middle, small_weight_left, small_weight_right]

#create a person for boxing (ready)
def boxing_person_ready (center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-33, 105)
    leg1center2 = center.clone()
    leg1center2.move(-10, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(15,100)
    leg2center2 = center.clone()
    leg2center2.move(40,197)
    leg2 = Line(leg2center1,leg2center2)
    leg2.setWidth(24)
    leg2.draw(win)

    arm_left_cneter1 = center.clone()
    arm_left_cneter1.move(-40, 40)
    arm_left_cneter2 = center.clone()
    arm_left_cneter2.move(-25, 70)
    arm_left = Line(arm_left_cneter1, arm_left_cneter2)
    arm_left.setWidth(11)

    arm_left1_cneter1 = center.clone()
    arm_left1_cneter1.move(-30, 70)
    arm_left1_cneter2 = center.clone()
    arm_left1_cneter2.move(-5, 46)
    arm_left1 = Line(arm_left1_cneter1, arm_left1_cneter2)
    arm_left1.setWidth(11)

    hand_left_center1 = center.clone()
    hand_left_center1.move(-5, 46)
    hand_left = Circle(hand_left_center1, 8)
    hand_left.setFill("white")

    arm_right = arm_left.clone()
    arm_right.move(66, 0)
    arm_right.draw(win)

    arm_right1 = arm_left1.clone()
    arm_right1.move(66, 0)
    arm_right1.draw(win)

    hand_right = hand_left.clone()
    hand_right.move(66, 0)
    hand_right.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    arm_left.draw(win)
    arm_left1.draw(win)
    hand_left.draw(win)

    return [head, body, leg1, leg2, arm_left, arm_left1, hand_left, arm_right, arm_right1, hand_right]


#create a person for boxing (fight_right)
def boxing_person_fight_right (center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-33, 105)
    leg1center2 = center.clone()
    leg1center2.move(-10, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(15,100)
    leg2center2 = center.clone()
    leg2center2.move(40,197)
    leg2 = Line(leg2center1,leg2center2)
    leg2.setWidth(24)
    leg2.draw(win)

    arm_left_cneter1 = center.clone()
    arm_left_cneter1.move(-40, 40)
    arm_left_cneter2 = center.clone()
    arm_left_cneter2.move(-25, 70)
    arm_left = Line(arm_left_cneter1, arm_left_cneter2)
    arm_left.setWidth(11)

    arm_left1_cneter1 = center.clone()
    arm_left1_cneter1.move(-30, 70)
    arm_left1_cneter2 = center.clone()
    arm_left1_cneter2.move(-5, 46)
    arm_left1 = Line(arm_left1_cneter1, arm_left1_cneter2)
    arm_left1.setWidth(11)

    hand_left_center1 = center.clone()
    hand_left_center1.move(-5, 46)
    hand_left = Circle(hand_left_center1, 8)
    hand_left.setFill("white")

    arm_right = arm_left.clone()
    arm_right.move(63, 0)
    arm_right.draw(win)

    arm_right1 = arm_left1.clone()
    arm_right1.move(63, 0)
    arm_right1.draw(win)

    hand_right = hand_left.clone()
    hand_right.move(63, 0)
    hand_right.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    arm_left_fight_center1 = center.clone()
    arm_left_fight_center1.move(-35, 40)
    arm_left_fight_center2 = center.clone()
    arm_left_fight_center2.move(70, 40)
    arm_left_fight = Line(arm_left_fight_center1, arm_left_fight_center2)
    arm_left_fight.setWidth(11)
    arm_left_fight.draw(win)

    hand_left_fight_center = center.clone()
    hand_left_fight_center.move(70, 40)
    hand_left_fight = Circle(hand_left_fight_center, 8)
    hand_left_fight.setFill("white")
    hand_left_fight.draw(win)


    return [head, body, leg1, leg2, arm_right, arm_right1, hand_right, arm_left_fight,hand_left_fight]

#create a person for boxing (fight_right)
def boxing_person_fight_left (center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-33, 105)
    leg1center2 = center.clone()
    leg1center2.move(-10, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(15,100)
    leg2center2 = center.clone()
    leg2center2.move(40,197)
    leg2 = Line(leg2center1,leg2center2)
    leg2.setWidth(24)
    leg2.draw(win)

    arm_left_cneter1 = center.clone()
    arm_left_cneter1.move(-40, 40)
    arm_left_cneter2 = center.clone()
    arm_left_cneter2.move(-25, 70)
    arm_left = Line(arm_left_cneter1, arm_left_cneter2)
    arm_left.setWidth(11)

    arm_left1_cneter1 = center.clone()
    arm_left1_cneter1.move(-30, 70)
    arm_left1_cneter2 = center.clone()
    arm_left1_cneter2.move(-5, 46)
    arm_left1 = Line(arm_left1_cneter1, arm_left1_cneter2)
    arm_left1.setWidth(11)

    hand_left_center1 = center.clone()
    hand_left_center1.move(-5, 46)
    hand_left = Circle(hand_left_center1, 8)
    hand_left.setFill("white")

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    arm_right_fight_center1 = center.clone()
    arm_right_fight_center1.move(35, 40)
    arm_right_fight_center2 = center.clone()
    arm_right_fight_center2.move(85, 40)
    arm_right_fight = Line(arm_right_fight_center1,arm_right_fight_center2)
    arm_right_fight.setWidth(11)
    arm_right_fight.draw(win)

    hand_right_fight_center = center.clone()
    hand_right_fight_center.move(85, 40)
    hand_right_fight = Circle(hand_right_fight_center, 8)
    hand_right_fight.setFill("white")
    hand_right_fight.draw(win)

    arm_left.draw(win)
    arm_left1.draw(win)
    hand_left.draw(win)

    return [head, body, leg1, leg2, arm_left,arm_left1,hand_left, arm_right_fight,hand_right_fight]

#create a sandbag for boxing
def sandbag_training(center, win):
    basecenter1 = center.clone()
    basecenter1.move(-85, -10)
    basecenter2 = center.clone()
    basecenter2.move(85, 10)
    base = Rectangle(basecenter1, basecenter2)
    base.setFill("black")
    base.draw(win)

    pole_vertical_center1 = center.clone()
    pole_vertical_center1.move(-10, -10)
    pole_vertical_center2 = center.clone()
    pole_vertical_center2.move(10, -340)
    pole_vertical = Rectangle(pole_vertical_center1, pole_vertical_center2)
    pole_vertical.setFill("black")
    pole_vertical.draw(win)

    pole_horizantal_center1 = center.clone()
    pole_horizantal_center1.move(-10, -340)
    pole_horizantal_center2 = center.clone()
    pole_horizantal_center2.move(-165, -320)
    pole_horizantal = Rectangle(pole_horizantal_center1, pole_horizantal_center2)
    pole_horizantal.setFill("black")
    pole_horizantal.draw(win)

    rope_center1 = center.clone()
    rope_center1.move(-159, -320)
    rope_center2 = center.clone()
    rope_center2.move(-165, -240)
    rope = Rectangle(rope_center1, rope_center2)
    rope.setFill("black")
    rope.draw(win)

    sandbag_center1 = center.clone()
    sandbag_center1.move(-202, -240)
    sandbag_center2 = center.clone()
    sandbag_center2.move(-122, -40)
    sandbag = Rectangle(sandbag_center1, sandbag_center2)
    sandbag.setFill("brown")
    sandbag.setOutline("brown")
    sandbag.draw(win)

    return [base, pole_vertical, pole_horizantal, rope, sandbag]

# create a squat person ready
def squat_person_ready(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm1center1 = center.clone()
    arm1center1.move(-35, 40)
    arm1center2 = center.clone()
    arm1center2.move(-60, -10)
    arm1 = Line(arm1center1, arm1center2)
    arm1.setWidth(10)
    arm1.draw(win)

    arm2center1 = center.clone()
    arm2center1.move(35, 40)
    arm2center2 = center.clone()
    arm2center2.move(60, -10)
    arm2 = Line(arm2center1, arm2center2)
    arm2.setWidth(10)
    arm2.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 105)
    leg1center2 = center.clone()
    leg1center2.move(-5, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 105)
    leg2center2 = center.clone()
    leg2center2.move(5, 200)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    return [head, body, arm1, arm2, leg1, leg2]

# create a squat person training
def squat_person_training (center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm1center1 = center.clone()
    arm1center1.move(-35, 40)
    arm1center2 = center.clone()
    arm1center2.move(-60, -10)
    arm1 = Line(arm1center1, arm1center2)
    arm1.setWidth(10)
    arm1.draw(win)

    arm2center1 = center.clone()
    arm2center1.move(35, 40)
    arm2center2 = center.clone()
    arm2center2.move(60, -10)
    arm2 = Line(arm2center1, arm2center2)
    arm2.setWidth(10)
    arm2.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 55)
    leg1center2 = center.clone()
    leg1center2.move(-5, 150)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 55)
    leg2center2 = center.clone()
    leg2center2.move(5, 150)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    return [head, body, arm1, arm2, leg1, leg2]

# create a squat person broken legs
def broken_legs_person(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm1center1 = center.clone()
    arm1center1.move(-35, 40)
    arm1center2 = center.clone()
    arm1center2.move(-60, 90)
    arm1 = Line(arm1center1, arm1center2)
    arm1.setWidth(10)
    arm1.draw(win)

    arm2center1 = center.clone()
    arm2center1.move(35, 40)
    arm2center2 = center.clone()
    arm2center2.move(60, 90)
    arm2 = Line(arm2center1, arm2center2)
    arm2.setWidth(10)
    arm2.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 105)
    leg1center2 = center.clone()
    leg1center2.move(-5, 155)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 105)
    leg2center2 = center.clone()
    leg2center2.move(5, 155)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    broken_leg1_center1 = center.clone()
    broken_leg1_center1.move(-11, 150)
    broken_leg1_center2 = center.clone()
    broken_leg1_center2.move(-55, 195)
    broken_leg1 = Line(broken_leg1_center1,broken_leg1_center2)
    broken_leg1.setFill("black")
    broken_leg1.setWidth(16)
    broken_leg1.draw(win)

    broken_leg2_center1 = center.clone()
    broken_leg2_center1.move(11,150)
    broken_leg2_center2 = center.clone()
    broken_leg2_center2.move(55,195)
    broken_leg2 = Line(broken_leg2_center1,broken_leg2_center2)
    broken_leg2.setFill("black")
    broken_leg2.setWidth(16)
    broken_leg2.draw(win)


    return [head, body, arm1, arm2, leg1, leg2,broken_leg1, broken_leg2]

# create a opponent be ready
def boxing_person_ready_opponent (center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(33, 105)
    leg1center2 = center.clone()
    leg1center2.move(10, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(-15,100)
    leg2center2 = center.clone()
    leg2center2.move(-40,197)
    leg2 = Line(leg2center1,leg2center2)
    leg2.setWidth(24)
    leg2.draw(win)

    arm_left_cneter1 = center.clone()
    arm_left_cneter1.move(40, 40)
    arm_left_cneter2 = center.clone()
    arm_left_cneter2.move(25, 70)
    arm_left = Line(arm_left_cneter1, arm_left_cneter2)
    arm_left.setWidth(11)

    arm_left1_cneter1 = center.clone()
    arm_left1_cneter1.move(30, 70)
    arm_left1_cneter2 = center.clone()
    arm_left1_cneter2.move(5, 46)
    arm_left1 = Line(arm_left1_cneter1, arm_left1_cneter2)
    arm_left1.setWidth(11)

    hand_left_center1 = center.clone()
    hand_left_center1.move(5, 46)
    hand_left = Circle(hand_left_center1, 8)
    hand_left.setFill("white")

    arm_right = arm_left.clone()
    arm_right.move(-66, 0)
    arm_right.draw(win)

    arm_right1 = arm_left1.clone()
    arm_right1.move(-66, 0)
    arm_right1.draw(win)

    hand_right = hand_left.clone()
    hand_right.move(-66, 0)
    hand_right.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("darkred")
    body.setOutline("darkred")
    body.draw(win)

    arm_left.draw(win)
    arm_left1.draw(win)
    hand_left.draw(win)

    return [head, body, leg1, leg2, arm_left, arm_left1, hand_left, arm_right, arm_right1, hand_right]

# create a opponent fight
def boxing_person_fight_right_opponent (center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(33, 105)
    leg1center2 = center.clone()
    leg1center2.move(10, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(-15,100)
    leg2center2 = center.clone()
    leg2center2.move(-40,197)
    leg2 = Line(leg2center1,leg2center2)
    leg2.setWidth(24)
    leg2.draw(win)

    arm_left_cneter1 = center.clone()
    arm_left_cneter1.move(40, 40)
    arm_left_cneter2 = center.clone()
    arm_left_cneter2.move(25, 70)
    arm_left = Line(arm_left_cneter1, arm_left_cneter2)
    arm_left.setWidth(11)

    arm_left1_cneter1 = center.clone()
    arm_left1_cneter1.move(30, 70)
    arm_left1_cneter2 = center.clone()
    arm_left1_cneter2.move(5, 46)
    arm_left1 = Line(arm_left1_cneter1, arm_left1_cneter2)
    arm_left1.setWidth(11)

    hand_left_center1 = center.clone()
    hand_left_center1.move(5, 46)
    hand_left = Circle(hand_left_center1, 8)
    hand_left.setFill("white")

    arm_right = arm_left.clone()
    arm_right.move(-63, 0)
    arm_right.draw(win)

    arm_right1 = arm_left1.clone()
    arm_right1.move(-63, 0)
    arm_right1.draw(win)

    hand_right = hand_left.clone()
    hand_right.move(-63, 0)
    hand_right.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("darkred")
    body.setOutline("darkred")
    body.draw(win)

    arm_left_fight_center1 = center.clone()
    arm_left_fight_center1.move(35, 40)
    arm_left_fight_center2 = center.clone()
    arm_left_fight_center2.move(-70, 40)
    arm_left_fight = Line(arm_left_fight_center1, arm_left_fight_center2)
    arm_left_fight.setWidth(11)
    arm_left_fight.draw(win)

    hand_left_fight_center = center.clone()
    hand_left_fight_center.move(-70, 40)
    hand_left_fight = Circle(hand_left_fight_center, 8)
    hand_left_fight.setFill("white")
    hand_left_fight.draw(win)

    return [head, body, leg1, leg2, arm_right, arm_right1, hand_right, arm_left_fight,hand_left_fight]


# create a opponent fight left
def boxing_person_fight_left_opponent(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(33, 105)
    leg1center2 = center.clone()
    leg1center2.move(10, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(-15,100)
    leg2center2 = center.clone()
    leg2center2.move(-40,197)
    leg2 = Line(leg2center1,leg2center2)
    leg2.setWidth(24)
    leg2.draw(win)

    arm_left_cneter1 = center.clone()
    arm_left_cneter1.move(40, 40)
    arm_left_cneter2 = center.clone()
    arm_left_cneter2.move(25, 70)
    arm_left = Line(arm_left_cneter1, arm_left_cneter2)
    arm_left.setWidth(11)

    arm_left1_cneter1 = center.clone()
    arm_left1_cneter1.move(30, 70)
    arm_left1_cneter2 = center.clone()
    arm_left1_cneter2.move(5, 46)
    arm_left1 = Line(arm_left1_cneter1, arm_left1_cneter2)
    arm_left1.setWidth(11)

    hand_left_center1 = center.clone()
    hand_left_center1.move(5, 46)
    hand_left = Circle(hand_left_center1, 8)
    hand_left.setFill("white")

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("darkred")
    body.setOutline("darkred")
    body.draw(win)

    arm_right_fight_center1 = center.clone()
    arm_right_fight_center1.move(-35, 40)
    arm_right_fight_center2 = center.clone()
    arm_right_fight_center2.move(-85, 40)
    arm_right_fight = Line(arm_right_fight_center1,arm_right_fight_center2)
    arm_right_fight.setWidth(11)
    arm_right_fight.draw(win)

    hand_right_fight_center = center.clone()
    hand_right_fight_center.move(-85, 40)
    hand_right_fight = Circle(hand_right_fight_center, 8)
    hand_right_fight.setFill("white")
    hand_right_fight.draw(win)

    arm_left.draw(win)
    arm_left1.draw(win)
    hand_left.draw(win)

    return [head, body, leg1, leg2, arm_left,arm_left1,hand_left, arm_right_fight,hand_right_fight]


# create a opponent lost
def person_lost_opponent(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm_left_center1 = center.clone()
    arm_left_center1.move(40, 35)
    arm_left_center2 = center.clone()
    arm_left_center2.move(80, -45)
    arm_left = Line(arm_left_center1, arm_left_center2)
    arm_left.setWidth(10)
    arm_left.draw(win)

    arm_right_center1 = center.clone()
    arm_right_center1.move(40, 35)
    arm_right_center2 = center.clone()
    arm_right_center2.move(80, 45)
    arm_right = Line(arm_right_center1, arm_right_center2)
    arm_right.setWidth(10)
    arm_right.draw(win)


    bodycenter1 = center.clone()
    bodycenter1.move(20, -35)
    bodycenter2 = center.clone()
    bodycenter2.move(105, 35)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("darkred")
    body.setOutline("darkred")
    body.draw(win)

    arm1_left1_2_center1 = center.clone()
    arm1_left1_2_center1.move(82, -45)
    arm1_left1_2_center2 = center.clone()
    arm1_left1_2_center2.move(95, -20)
    arm1_left1_2 = Line(arm1_left1_2_center1, arm1_left1_2_center2)
    arm1_left1_2.setWidth(10)
    arm1_left1_2.draw(win)

    arm1_right1_2_center1 = center.clone()
    arm1_right1_2_center1.move(82, 45)
    arm1_right1_2_center2 = center.clone()
    arm1_right1_2_center2.move(106, 70)
    arm1_right1_2 = Line(arm1_right1_2_center1, arm1_right1_2_center2)
    arm1_right1_2.setWidth(10)
    arm1_right1_2.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(105, -25)
    leg1center2 = center.clone()
    leg1center2.move(155, -5)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(105, 25)
    leg2center2 = center.clone()
    leg2center2.move(155, 5)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    broken_leg1_center1 = center.clone()
    broken_leg1_center1.move(150, -17)
    broken_leg1_center2 = center.clone()
    broken_leg1_center2.move(195, 15)
    broken_leg1 = Line(broken_leg1_center1, broken_leg1_center2)
    broken_leg1.setFill("black")
    broken_leg1.setWidth(16)
    broken_leg1.draw(win)

    broken_leg2_center1 = center.clone()
    broken_leg2_center1.move(150, 11)
    broken_leg2_center2 = center.clone()
    broken_leg2_center2.move(195, 55)
    broken_leg2 = Line(broken_leg2_center1, broken_leg2_center2)
    broken_leg2.setFill("black")
    broken_leg2.setWidth(16)
    broken_leg2.draw(win)


    return [head,arm_left, arm_right, arm1_right1_2, arm1_right1_2, body, leg1, leg2, broken_leg1, broken_leg2]


# create a player lost
def person_lost(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm_left_center1 = center.clone()
    arm_left_center1.move(-40, 35)
    arm_left_center2 = center.clone()
    arm_left_center2.move(-80, -45)
    arm_left = Line(arm_left_center1, arm_left_center2)
    arm_left.setWidth(10)
    arm_left.draw(win)

    arm_right_center1 = center.clone()
    arm_right_center1.move(-40, 35)
    arm_right_center2 = center.clone()
    arm_right_center2.move(-80, 45)
    arm_right = Line(arm_right_center1, arm_right_center2)
    arm_right.setWidth(10)
    arm_right.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-20, 35)
    bodycenter2 = center.clone()
    bodycenter2.move(-105, -35)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    arm1_left1_2_center1 = center.clone()
    arm1_left1_2_center1.move(-82, -45)
    arm1_left1_2_center2 = center.clone()
    arm1_left1_2_center2.move(-95, -20)
    arm1_left1_2 = Line(arm1_left1_2_center1, arm1_left1_2_center2)
    arm1_left1_2.setWidth(10)
    arm1_left1_2.draw(win)

    arm1_right1_2_center1 = center.clone()
    arm1_right1_2_center1.move(-82, 45)
    arm1_right1_2_center2 = center.clone()
    arm1_right1_2_center2.move(-106, 70)
    arm1_right1_2 = Line(arm1_right1_2_center1, arm1_right1_2_center2)
    arm1_right1_2.setWidth(10)
    arm1_right1_2.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-105, -25)
    leg1center2 = center.clone()
    leg1center2.move(-155, -5)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(-105, 25)
    leg2center2 = center.clone()
    leg2center2.move(-155, 5)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    broken_leg1_center1 = center.clone()
    broken_leg1_center1.move(-150, -17)
    broken_leg1_center2 = center.clone()
    broken_leg1_center2.move(-195, 15)
    broken_leg1 = Line(broken_leg1_center1, broken_leg1_center2)
    broken_leg1.setFill("black")
    broken_leg1.setWidth(16)
    broken_leg1.draw(win)

    broken_leg2_center1 = center.clone()
    broken_leg2_center1.move(-150, 11)
    broken_leg2_center2 = center.clone()
    broken_leg2_center2.move(-195, 55)
    broken_leg2 = Line(broken_leg2_center1, broken_leg2_center2)
    broken_leg2.setFill("black")
    broken_leg2.setWidth(16)
    broken_leg2.draw(win)

    return [head,arm_left, arm_right, arm1_right1_2, arm1_right1_2, body, leg1, leg2, broken_leg1, broken_leg2]


# create a player wins
def person_won(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm1center1 = center.clone()
    arm1center1.move(-35, 40)
    arm1center2 = center.clone()
    arm1center2.move(-60, -10)
    arm1 = Line(arm1center1, arm1center2)
    arm1.setWidth(10)
    arm1.draw(win)

    arm2center1 = center.clone()
    arm2center1.move(35, 40)
    arm2center2 = center.clone()
    arm2center2.move(60, -10)
    arm2 = Line(arm2center1, arm2center2)
    arm2.setWidth(10)
    arm2.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("skyblue")
    body.setOutline("skyblue")
    body.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 105)
    leg1center2 = center.clone()
    leg1center2.move(-5, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 105)
    leg2center2 = center.clone()
    leg2center2.move(5, 200)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    return [head, body, arm1, arm2, leg1, leg2]


# create a opponent wins
def person_won_opponent(center, win):
    head = Circle(center, 20)
    head.setFill("white")
    head.draw(win)

    arm1center1 = center.clone()
    arm1center1.move(-35, 40)
    arm1center2 = center.clone()
    arm1center2.move(-60, -10)
    arm1 = Line(arm1center1, arm1center2)
    arm1.setWidth(10)
    arm1.draw(win)

    arm2center1 = center.clone()
    arm2center1.move(35, 40)
    arm2center2 = center.clone()
    arm2center2.move(60, -10)
    arm2 = Line(arm2center1, arm2center2)
    arm2.setWidth(10)
    arm2.draw(win)

    bodycenter1 = center.clone()
    bodycenter1.move(-35, 20)
    bodycenter2 = center.clone()
    bodycenter2.move(35, 105)
    body = Rectangle(bodycenter1, bodycenter2)
    body.setFill("darkred")
    body.setOutline("darkred")
    body.draw(win)

    leg1center1 = center.clone()
    leg1center1.move(-25, 105)
    leg1center2 = center.clone()
    leg1center2.move(-5, 200)
    leg1 = Rectangle(leg1center1, leg1center2)
    leg1.setFill("black")
    leg1.draw(win)

    leg2center1 = center.clone()
    leg2center1.move(25, 105)
    leg2center2 = center.clone()
    leg2center2.move(5, 200)
    leg2 = Rectangle(leg2center1, leg2center2)
    leg2.setFill("black")
    leg2.draw(win)

    return [head, body, arm1, arm2, leg1, leg2]


#delete a graphic
def undraw(draw_list):
    for darw in draw_list:
        darw.undraw()

#create a button for choosing weight
def button_for_weight(center, weight, win):
    button_center1 = center.clone()
    button_center1.move(-50, -25)
    button_center2 = center.clone()
    button_center2.move(50, 25)
    button = Rectangle(button_center1, button_center2)

    center_for_kg = center.clone()
    center_for_kg.move(10,0)
    weight_kg = Text(center_for_kg,"kg").draw(win)

    center_for_weighttext = center.clone()
    center_for_weighttext.move(-10,0)
    weight_number = Text(center_for_weighttext,weight).draw(win)

    button.draw(win)
    return [button,weight_kg,weight_number]

#Refresh texts in rooms
def show_text1(message, win):
    global text_ui1
    if text_ui1 is None:
        text_ui1 = Text(Point(500, 180), message)
        text_ui1.draw(win)
    else:
        text_ui1.setText(message)

#text for sprint room
def show_text2(message, win):
    global text_ui2
    if text_ui2 is None:
        text_ui2 = Text(Point(500, 90), message)
        text_ui2.draw(win)
    else:
        text_ui2.setText(message)

#test for boxing room
def show_text_boxing_room(message, win):
    global text_boxing_room
    if text_boxing_room is None:
        text_boxing_room = Text(Point(500, 100), message)
        text_boxing_room.draw(win)
    else:
        text_boxing_room.setText(message)

#test for leg training room
def show_text_leg_training_room(message, win):
    global text_leg_training_room
    if text_leg_training_room is None:
        text_leg_training_room = Text(Point(500, 100), message)
        text_leg_training_room.draw(win)
    else:
        text_leg_training_room.setText(message)

#test for final challenge room
def show_text_final_chanllenge(message, win):
    global text_final_chanllenge
    if text_final_chanllenge is None:
        text_final_chanllenge = Text(Point(500, 65), message)
        text_final_chanllenge.draw(win)
    else:
        text_final_chanllenge.setText(message)

#Show the user's current level
def show_level(win):
    person_description = f'Your current level is {person_level * level_multi}'
    global level_ui
    if level_ui is None:
        level_ui = Text(Point(111, 80), person_description)
        level_ui.draw(win)
    else:
        level_ui.setText(person_description)

#Show the user's inventory level
def show_inventory_level(win):
    invenotry_description = f'Your current level is {inventory_award}'
    global inventory_ui
    #if no inventory, don't show
    if inventory_ui is None:
        inventory_ui = Text(Point(111, 80), invenotry_description)
        inventory_ui.draw(win)
    else:
        inventory_ui.setText(invenotry_description)

#Show the user's inventory items
def show_inventory_items(win):
    global person_level
    invenotry_items1 = f'Now you have {inventory} in your inventory,' \
                       f' \nyou can get an additional {inventory_award} level up, now your level is {person_level + inventory_award}' \
                       f' \n\n # <Fighting Gloves> 5 points, <Red Bull> 5 points, <Fighting Guide> 10 points, <Pain killer> 10 points  #'
    global inventory_items
    # if no inventory, don't show
    if inventory_items is None:
        inventory_items = Text(Point(500, 132), invenotry_items1)
        inventory_items.draw(win)
    else:
        inventory_ui.setText(invenotry_items1)



# create an arm training room
def arms_training_room1():
    global person_level
    global level_multi
    global level_history_room
    global level_history_level
    global inventory
    global inventory_award
    global player_action
    import time

    arms_training_room = GraphWin("Arms Training room", 1000, 800)
    arms_training_room.setBackground("white")

    ground = Rectangle(Point(0, 500), Point(1000, 800))
    ground.setOutline("khaki")
    ground.setFill("khaki")
    ground.draw(arms_training_room)

    show_text2("Please choose your weight for exercise"
                        "\nCaution! you only have one chance, you may pass or fail", arms_training_room)
    button_for_weight(Point(350,175),10,arms_training_room)
    button_for_weight(Point(500,175),20,arms_training_room)
    button_for_weight(Point(650,175),30,arms_training_room)

    original_perosn = person(Point(300, 400), arms_training_room)
    original_small_weight = small_weight(Point(600,590),arms_training_room)
    original_small_weight1 = small_weight(Point(700, 590), arms_training_room)

    while True:
        click = arms_training_room.getMouse()
        #10kg
        #button for checking
        if click.getX() <= 400 and click.getX() >= 300 and click.getY() <= 200 and click.getY() >= 150:
            player_action.append('choose 10kg weight for arms')
            show_text2("Exercise ongoing......",arms_training_room)
            for perosn_objects in original_perosn:
                perosn_objects.undraw()

            for weight_objects in original_small_weight:
                weight_objects.undraw()

            for weight_objects1 in original_small_weight1:
                weight_objects1.undraw()
            # Repeat the actions 5 times
            for i in range (5):
                exercise_person1 = exercise_person(Point(600, 400), arms_training_room)
                small_weight_list1 = small_weight(Point(545, 450),arms_training_room)
                small_weight_list2 = small_weight(Point(655, 450),arms_training_room)
                time.sleep(1)
                undraw(small_weight_list1)
                undraw(small_weight_list2)
                undraw(exercise_person1)
                retire_person = person(Point(600, 400), arms_training_room)
                small_weight_list1 = small_weight(Point(545, 485), arms_training_room)
                small_weight_list2 = small_weight(Point(655,485),arms_training_room)
                time.sleep(1)
                undraw(small_weight_list1)
                undraw(small_weight_list2)
                undraw(retire_person)

            person(Point(300,400),arms_training_room)
            small_weight(Point(600, 590), arms_training_room)
            small_weight(Point(700, 590), arms_training_room)
            show_text2("Opps, the weight you chose is a bit light, but you can continue"
                       "\n level +5\n"
                       "\n press <space> to exit the room", arms_training_room)
            level_history_level.append(person_level + 5)
            person_level += 5

            arms_training_room.getKey()
            player_action.append('exit arms training room')
            arms_training_room.close()

            return arms_training_room


        #20 kg
        # button for checking
        elif click.getX() <= 550 and click.getX() >= 450 and click.getY() <= 200 and click.getY() >= 150:
            player_action.append('choose 20kg weight for arms')
            show_text2("Exercise ongoing......", arms_training_room)
            for perosn_objects in original_perosn:
                perosn_objects.undraw()

            for weight_objects in original_small_weight:
                weight_objects.undraw()

            for weight_objects1 in original_small_weight1:
                weight_objects1.undraw()

            # Repeat the actions 5 times
            for i in range(5):
                exercise_person1 = exercise_person(Point(600, 400), arms_training_room)
                small_weight_list1 = small_weight(Point(545, 450), arms_training_room)
                small_weight_list2 = small_weight(Point(655, 450), arms_training_room)
                time.sleep(1)
                undraw(small_weight_list1)
                undraw(small_weight_list2)
                undraw(exercise_person1)
                retire_person = person(Point(600, 400), arms_training_room)
                small_weight_list1 = small_weight(Point(545, 485), arms_training_room)
                small_weight_list2 = small_weight(Point(655, 485), arms_training_room)
                time.sleep(1)
                undraw(small_weight_list1)
                undraw(small_weight_list2)
                undraw(retire_person)

            person(Point(300,400),arms_training_room)
            small_weight(Point(600, 590), arms_training_room)
            small_weight(Point(700, 590), arms_training_room)
            fighting_guide = Image(Point(500,400),"kung fu.gif")
            fighting_guide.draw(arms_training_room)
            show_text2("Congratulations!!! "
                       "\nYou chose the right weight and you get a prize <Fighting Guide> for your inventory!"
                       "\n level +10\n"
                       "\n press <space> to exit the room", arms_training_room)
            inventory.append("Fighting Guide")
            inventory_award += 15
            level_history_level.append(person_level + 10)
            person_level += 10

            arms_training_room.getKey()
            player_action.append('exit arms training room')
            arms_training_room.close()

            return arms_training_room


        #30kg arms broken
        # button for checking
        elif click.getX() <= 700 and click.getX() >= 600 and click.getY() <= 200 and click.getY() >= 150:
            player_action.append('choose 30kg weight for arms')
            show_text2("Exercise ongoing......", arms_training_room)
            for perosn_objects in original_perosn:
                perosn_objects.undraw()

            for weight_objects in original_small_weight:
                weight_objects.undraw()

            for weight_objects1 in original_small_weight1:
                weight_objects1.undraw()

            # Repeat the actions 5 times
            for i in range(5):
                exercise_person1 = exercise_person(Point(600, 400), arms_training_room)
                small_weight_list1 = small_weight(Point(545, 450), arms_training_room)
                small_weight_list2 = small_weight(Point(655, 450), arms_training_room)
                time.sleep(1)
                undraw(small_weight_list1)
                undraw(small_weight_list2)
                undraw(exercise_person1)
                retire_person = person(Point(600, 400), arms_training_room)
                small_weight_list1 = small_weight(Point(545, 485), arms_training_room)
                small_weight_list2 = small_weight(Point(655, 485), arms_training_room)
                time.sleep(1)
                undraw(small_weight_list1)
                undraw(small_weight_list2)
                undraw(retire_person)

            broken_arm_person(Point(300, 400), arms_training_room)
            small_weight(Point(600, 590), arms_training_room)
            small_weight(Point(700, 590), arms_training_room)
            show_text2("OH no! Your weight is too heavy! You broke you arms!"
                       "\n level -10\n"
                       "\n press <space> to exit the room", arms_training_room)
            level_history_level.append(person_level - 10)
            person_level -= 10

            arms_training_room.getKey()
            player_action.append('exit arms training room')
            arms_training_room.close()

            return arms_training_room

# cover for running person background
def cover(center,win):

    center1 = center.clone()
    center1.move(-80,-110)
    center2 = center.clone()
    center2.move(80,10)
    cover_man = Rectangle(center1,center2)
    cover_man.setFill("white")
    cover_man.setOutline("white")
    cover_man.draw(win)

    center3 = center.clone()
    center3.move(-80, 10)
    center4 = center.clone()
    center4.move(80, 110)
    cover_man1 = Rectangle(center3, center4)
    cover_man1.setFill("darkred")
    cover_man1.setOutline("darkred")
    cover_man1.draw(win)

    return[cover_man,cover_man1]


# Create a sprint room
def sprint_room1():
    import time
    global person_level
    global inventory
    global inventory_award
    global player_action
    global level_history_level

    sprint_room = GraphWin("Room for sprint exercise",1000,800)
    sprint_room.setBackground("white")

    show_text1(
        "This is a sprint exercise,click the mouse as quick as you can to run"
               "\n your sprint time will be measured, try to get to the destination in 17s to win a reward,"
               "\n Caution! you only have one chance, you may also fail if you take more than 18.5s",
        sprint_room)
    race_lane = Rectangle(Point(0,750),Point(1000,500))
    race_lane.setFill("darkred")
    race_lane.setOutline("darkred")
    race_lane.draw(sprint_room)

    race_lane1 = Rectangle(Point(0,620),Point(1000,630))
    race_lane1.setFill("white")
    race_lane1.setOutline("white")
    race_lane1.draw(sprint_room)

    race_lane3 = Rectangle(Point(970, 500), Point(1000, 750))
    race_lane3.setFill("black")
    race_lane3.draw(sprint_room)

    #set original coordinates for cover
    x1 = 100
    y1 = 490
    z1 = Point(x1, y1)
    cover(z1, sprint_room)

    # set original coordinates for  person
    x = 100
    y = 400
    z = Point(x, y)
    person(z, sprint_room)

    race_lane2 = Rectangle(Point(0, 500), Point(30, 750))
    race_lane2.setFill("black")
    race_lane2.draw(sprint_room)

    sprint_room.getMouse()
    player_action.append("start running")
    start_time = time.time()
    show_text1("Come On! Run! Run! Run!",sprint_room)

    # a loop for running, once the user clicks mouse, the person and cover move
    while x1 <= 900:
        x1 = x1 + 15
        y1 = 490
        z1 = Point(x1, y1)
        cover(z1, sprint_room)

        x = x + 15
        y = 400
        z = Point(x, y)
        running_person(z, sprint_room)

        race_lane3 = Rectangle(Point(970, 500), Point(1000, 750))
        race_lane3.setFill("black")
        race_lane3.draw(sprint_room)

        sprint_room.getMouse()
    # count time
    end_time = time.time()
    time_elasped = end_time - start_time

    # compare player's time with the requirement
    if time_elasped <= 17:
        show_text1(
            f"Congratulation!!!"
            f"\n You have passed the exercise in {round(time_elasped,2)}s, and you get a Red Bull for your inventory,"
            f"\n level +10\n"
            f"\n press <space> to exit the room",
            sprint_room)
        red_bull = Image(Point(500,350),"red bull.gif")
        red_bull.draw(sprint_room)
        level_history_level.append(person_level + 10)
        person_level += 10
        inventory.append("Red Bull")
        inventory_award += 5
    elif time_elasped >17 and time_elasped <= 18.5:
        show_text1(
            f" Not bad! You have passed the exercise in {round(time_elasped, 2)}s, but you could be faster,"
            f"\n level +5\n"
            f"\n press <space> to exit the room",
            sprint_room)
        level_history_level.append(person_level + 5)
        person_level += 5
    else:
        show_text1(
            f" Sorry You took too long in the sprint, {round(time_elasped, 2)}s,you failed the exercise,"
            f"\n level -5\n"
            f"\n press <space> to exit the room",
            sprint_room)
        level_history_level.append(person_level - 5)
        person_level -= 5
    sprint_room.getKey()
    player_action.append("exit sprint room")
    sprint_room.close()

    return sprint_room

# create a boxing room
def boxing_room():
    from random import randrange
    global person_level
    global inventory
    global inventory_award
    global player_action
    global level_history_level

    win = GraphWin("boxing_room",1000,800)
    win.setBackground("white")

    ground = Rectangle(Point(0,500),Point(1000,800))
    ground.setOutline("grey")
    ground.setFill("grey")
    ground.draw(win)

    show_text_boxing_room("This is a boxing room, you can practise with a sandbag "
                          "\n click anywhere to get ready,try to get 115 points for a prize",
                          win)

    original_person = person(Point(200,400),win)

    win.getMouse()

    player_action.append("get ready for boxing")
    undraw(original_person)

    show_text_boxing_room("Ok now you are ready to fight, click the red area on the sandbag to fight, click until it stops", win)

    sandbag_training(Point(785,590),win)

    ready_perosn = boxing_person_ready(Point(500, 400), win)
    # Create a target to hit
    target = Circle(Point(623,450),13)
    target.setFill("red")
    target.draw(win)

    total_points = 0
    total_points1 = 0

    while True:
        click = win.getMouse()
        #button for start
        if click.getX() <= 636 and click.getX() >= 610 and click.getY() <= 463 and click.getY() >= 437:
            show_text_boxing_room("Come On! fight! fight! fight!", win)
            player_action.append("start boxing training")
            # a loop repeat 10 times, generate random points from each hit and sum the total
            for i in range (10):
                undraw(ready_perosn)
                fight_right = boxing_person_fight_right(Point(530, 400), win)
                win.getMouse()
                points = randrange(1,12)
                show_text_boxing_room(f"You get {points} points for this hit!",win)
                total_points += points
                undraw(fight_right)
                fight_left = boxing_person_fight_left(Point(530,400),win)
                win.getMouse()
                points1 = randrange(1, 10)
                show_text_boxing_room(f"You get {points1} points for this hit!",win)
                total_points1 += points1
                undraw(fight_left)
            break

    total_points_point1 = total_points +total_points1
    #compare the player's data with the requirements
    if total_points_point1 >= 115:
        show_text_boxing_room(
            f"Awesome! You finished the boxing exercise, the total points you get is {total_points_point1} and you get a nice fighting gloves "
            f"\n Level +10\n"
            f"\n Press <space> to exit",
            win)
        fighting_gloves = Image(Point(250, 400), "fighting gloves.gif")
        fighting_gloves.draw(win)
        level_history_level.append(person_level + 10)
        person_level += 10
        inventory.append("Fighting Gloves")
        inventory_award += 5

    elif total_points_point1 >=90 and total_points_point1 < 115:
        show_text_boxing_room(
            f"Not bad! you finished the boxing exercise, the total points you get is {total_points_point1}. Keep Going! "
            f"\n Level +5\n"
            f"\n Press <space> to exit",
            win)
        level_history_level.append(person_level + 5)
        person_level += 5

    else:
        show_text_boxing_room(
            f"Oh no! you are unlucky, the total points you get is too low, only {total_points_point1}. You can be better! "
            f"\n Level -5\n"
            f"\n Press <space> to exit",
            win)
        level_history_level.append(person_level - 5)
        person_level -= 5

    ready_perosn = boxing_person_ready(Point(500, 400), win)

    win.getKey()
    player_action.append("exit boxing room")
    win.close()

    return win

#create a legs training room
def leg_training_room():
    global person_level
    global inventory
    global inventory_award
    global level_history_level
    import time


    leg_training_room = GraphWin("leg_training room",1000,800)
    leg_training_room.setBackground("white")

    show_text_leg_training_room("You have entered the training room for legs. Please choose the correct weight for squat. "
                                "\nCaution！you only have one chance you may pass or fail", leg_training_room)

    button_for_weight(Point(350, 175), 60, leg_training_room)
    button_for_weight(Point(500, 175), 90, leg_training_room)
    button_for_weight(Point(650, 175), 120, leg_training_room)

    ground = Rectangle(Point(0, 500), Point(1000, 800))
    ground.setOutline("khaki")
    ground.setFill("khaki")
    ground.draw(leg_training_room)

    original_person = person(Point(200, 400), leg_training_room)
    original_weight = weight(Point(500, 570),leg_training_room)

    while True:
        click = leg_training_room.getMouse()
        #60kg
        #button for choosing
        if click.getX() <= 400 and click.getX() >= 300 and click.getY() <= 200 and click.getY() >= 150:
            show_text_leg_training_room("Exercise ongoing......",leg_training_room)
            player_action.append("choose 60kg weight for legs")
            undraw(original_person)
            undraw(original_weight)
            #Repeat 10 times automatically
            for i in range (10):
                weight_up = weight(Point(500,420),leg_training_room)
                person_up = squat_person_ready(Point(500,420),leg_training_room)
                time.sleep(1)
                undraw(weight_up)
                undraw(person_up)
                weight_down = weight(Point(500,470),leg_training_room)
                person_down = squat_person_training(Point(500,470),leg_training_room)
                time.sleep(1)
                undraw(weight_down)
                undraw(person_down)

            person(Point(200, 400), leg_training_room)
            weight(Point(500, 570), leg_training_room)
            show_text_leg_training_room("Opps, the weight you chose is a bit light, but you can continue"
                       "\n level +5 \n\n press <space> to exit the room", leg_training_room)
            level_history_level.append(person_level + 5)
            person_level += 5

            leg_training_room.getKey()
            leg_training_room.close()

            return leg_training_room


        # 90 kg
        # button for choosing
        elif click.getX() <= 550 and click.getX() >= 450 and click.getY() <= 200 and click.getY() >= 150:
            show_text_leg_training_room("Exercise ongoing......", leg_training_room)
            player_action.append("choose 90kg weight for legs")
            undraw(original_person)
            undraw(original_weight)
            # Repeat 10 times automatically
            for i in range(10):
                weight_up = weight(Point(500, 420), leg_training_room)
                person_up = squat_person_ready(Point(500, 420), leg_training_room)
                time.sleep(1)
                undraw(weight_up)
                undraw(person_up)
                weight_down = weight(Point(500, 470), leg_training_room)
                person_down = squat_person_training(Point(500, 470), leg_training_room)
                time.sleep(1)
                undraw(weight_down)
                undraw(person_down)

            person(Point(200, 400),leg_training_room)
            weight(Point(500, 570), leg_training_room)
            show_text_leg_training_room("Congratulations!! You chose the correct weight and you get a prize <Pain Killer> for the final combat!"
                "\n level +10 \n\n press <space> to exit the room", leg_training_room)
            pain_killer = Image(Point(500,400),"pain killer.gif")
            pain_killer.draw(leg_training_room)
            level_history_level.append(person_level + 10)
            person_level += 10
            inventory.append("Pain Killer")
            inventory_award += 10

            leg_training_room.getKey()
            leg_training_room.close()

            return leg_training_room


        # 120 kg
        # button for choosing
        elif click.getX() <= 700 and click.getX() >= 600 and click.getY() <= 200 and click.getY() >= 150:
            show_text_leg_training_room("Exercise ongoing......", leg_training_room)
            player_action.append("choose 120kg weight for legs")
            undraw(original_person)
            undraw(original_weight)
            # Repeat 10 times automatically
            for i in range(10):
                weight_up = weight(Point(500, 420), leg_training_room)
                person_up = squat_person_ready(Point(500, 420), leg_training_room)
                time.sleep(1)
                undraw(weight_up)
                undraw(person_up)
                weight_down = weight(Point(500, 470), leg_training_room)
                person_down = squat_person_training(Point(500, 470), leg_training_room)
                time.sleep(1)
                undraw(weight_down)
                undraw(person_down)

            broken_legs_person(Point(200, 400), leg_training_room)
            weight(Point(500, 570), leg_training_room)
            show_text_leg_training_room("OH no! You weight is too heavy! You broke your legs!"
                       "\n level -10 \n\n press <space> to exit the room", leg_training_room)
            level_history_level.append(person_level - 10)
            person_level -= 10

            leg_training_room.getKey()
            player_action.append("exit legs training room")
            leg_training_room.close()

            return leg_training_room

#create a final challenge room
def final_chanllenge_room():
    global inventory_award
    global inventory
    global person_level
    global level_history_level
    import time
    win = GraphWin("final challenge room", 1000, 800)
    win.setBackground("white")

    background = Rectangle(Point(150,200),Point(850,700))
    background.setWidth(5)
    background.setFill("khaki")
    background.draw(win)
    level_history_level.append(person_level + inventory_award)
    #show inventory if the player has (text)
    #Inventory is used in the final challenge room to give player extra level up
    if inventory_award >0:
        show_inventory_items(win)
        person_level += inventory_award
    show_text_final_chanllenge("Welcome! This is the final challenge. You will fight with the boss of level 50,"
                               "\n click anywhere to fight ",win)

    original_person = person(Point(300, 350), win)

    original_opponent = boxing_person_ready_opponent(Point(720,350),win)
    # check and show which inventory the player has (images)
    if "Pain Killer" in inventory:
        pain_killer = Image(Point(70, 280), "pain killer.gif")
        pain_killer.draw(win)
    if "Fighting Gloves" in inventory:
        fighting_gloves = Image(Point(930, 280), "fighting gloves.gif")
        fighting_gloves.draw(win)
    if "Red Bull" in inventory:
        red_bull = Image(Point(70, 100), "red bull.gif")
        red_bull.draw(win)
    if "Fighting Guide" in inventory:
        fighting_guide = Image(Point(930, 100), "kung fu.gif")
        fighting_guide.draw(win)

    win.getMouse()
    player_action.append("start fighting with the boss")
    undraw(original_person)
    undraw(original_opponent)

    show_text_final_chanllenge("Fighting......xxxx....xxxx....",
                               win)

    #Compare the player's level with the oppnent's level(40)
    #the player won
    if person_level >= 50:
        #a loop repeat 10 times fight automatically
        for i in range(10):
            fight_right_opponent = boxing_person_fight_right_opponent(Point(560,350),win)
            fight_left = boxing_person_fight_left(Point(440, 350), win)
            time.sleep(0.5)
            undraw(fight_right_opponent)
            undraw(fight_left)
            fight_left_opponent = boxing_person_fight_left_opponent(Point(560,350),win)
            fight_right = boxing_person_fight_right(Point(440,350),win)
            time.sleep(0.5)
            undraw(fight_left_opponent)
            undraw(fight_right)
        person_lost_opponent(Point(500, 460), win)
        person_won(Point(400,350),win)
        show_text_final_chanllenge("Oh yeah! you beat him!. You are the winner! "
                                   "\n press <space> to exit",win)
        win.getKey()
        player_action.append("exit the final challenge room")
        win.close()
        return win

    #the player lost
    else:
        # a loop repeat 10 times fight automatically
        for i in range(10):
            fight_right_opponent = boxing_person_fight_right_opponent(Point(560,350),win)
            fight_left = boxing_person_fight_left(Point(440, 350), win)
            time.sleep(0.5)
            undraw(fight_right_opponent)
            undraw(fight_left)
            fight_left_opponent = boxing_person_fight_left_opponent(Point(560,350),win)
            fight_right = boxing_person_fight_right(Point(440,350),win)
            time.sleep(0.5)
            undraw(fight_left_opponent)
            undraw(fight_right)
        person_lost(Point(470,460), win)
        person_won_opponent(Point(570,350),win)
        show_text_final_chanllenge("Oh No! your level is below your opponent's level! You lost the game."
                                   "\n press <space> to exit", win)

        win.getKey()
        player_action.append("exit the final challenge room")
        win.close()
        return win


#Refresh text in command function
def show_text_command1(message, win):
    global text_ui
    if text_ui is None:
        text_ui = Text(Point(195, 180), message)
        text_ui.draw(win)
    else:
        text_ui.setText(message)

def show_text_command(message, win):
    global text_command
    if text_command is None:
        text_command = Text(Point(132, 100), message)
        text_command.draw(win)
    else:
        text_command.setText(message)

def show_text_command2 (message, win):
    global text_command2
    if text_command2 is None:
        text_command2 = Text(Point(205, 120), message)
        text_command2.draw(win)
    else:
        text_command2.setText(message)

def show_text_command3_final(message, win):
    global text_command3_final
    if text_command3_final is None:
        text_command3_final = Text(Point(830,60), message)
        text_command3_final.draw(win)
    else:
        text_command3_final.setText(message)

# Output user's action to a file
def output_data():
    outputpa = open("player actions.txt", "w")

    for line in player_action:
        print(line, file=outputpa)

    outputpa.close()

# Output user's level analysis to a line chart
def output_level():
    global level_history_level
    global level_history_room
    import matplotlib.pyplot as plt

    levels = level_history_level
    lables = level_history_room
    plt.xlabel("Rooms")
    plt.ylabel("Levels")
    plt.title("Player's performance analysis\nYour level history in different rooms")

    plt.plot(lables,levels,"o--")
    plt.show()


# Set orders in the welcome page, allow user to go different directions and choose different rooms
def command(win):
    global person_level
    global level_multi
    global visited_room
    global player_action
    #print(inventory)
    #print(inventory_award)
    #print(player_action)
    #print(level_history_level)
    #print(level_history_room)
    original_person = person(Point(500, 300), win)
    show_level(win)
    show_text_command(
        "which way you want to go first?",
        win)
    show_text_command2(
        "type in <go north>,<go south>,<go east>,<go west>",
        win)
    show_text_command3_final(
        "You will have a final challenge "
        "\nafter the trainings",
        win)
    #Check if the player has gone through all the rooms
    if "north" in visited_room and "east" in visited_room and "south" in visited_room and "west" in visited_room and "final" in visited_room:
        output_data()
        undraw(original_person)
        Text(Point(500, 362), "Congratulations! Now you finished the game, here you will have your analysis"
                              "\nThe players action report has been saved in the file <player actions.txt>\n"
                              "\nNow you can click anywhere to leave. See you next time!").draw(win)
        output_level()
        win.getMouse()
        quit()

    # Check if the player has gone through all the trainings
    elif "north" in visited_room and "east" in visited_room and "south" in visited_room and "west" in visited_room:
        final_chanllenge = Rectangle(Point(770, 110), Point(830, 140))
        final_chanllenge.setFill("black")
        final_chanllenge.draw(win)
        show_text_command3_final("Ok Now you finished all the trainings. "
                                 "\n You can go to the final challenge \nClick the black button to confirm",
                                 win)

    inputbox = Entry(Point(75, 150), 10)
    inputbox.draw(win)
    cilck1 = win.getMouse()
    command_walk = inputbox.getText()

    #Input validation: check if the user types go south
    if command_walk == "go south":
        # check if the user has visited the room
        if 'south' in visited_room:
            show_text_command1 ("you have already entered this room,\nplease try the other rooms",win)
            for person_objects in original_person:
                person_objects.undraw()
            command(win)
        visited_room.append("south")
        player_action.append('go south')
        for person_objects in original_person:
            person_objects.undraw()
        person_list = person(Point(630, 550), win)

        show_text_command1("you are about to enter room 1,\n click the door to enter", win)
        while True:
            x = win.getMouse()
            if x.getX() <= 570 and x.getX() >= 430 and x.getY() <= 755 and x.getY() >= 555:
                player_action.append('enter arms training room')
                arms_training_room1()
                level_history_room.append('arms')
                break
        for person_obj in person_list:
            person_obj.undraw()
        command(win)

    # Input validation: check if the user types go north
    elif command_walk == "go north":
        # check if the user has visited the room
        if 'north' in visited_room:
            show_text_command1("you have already entered this room,\nplease try the other rooms", win)
            for person_objects in original_person:
                person_objects.undraw()
            command(win)
        visited_room.append("north")
        player_action.append('go north')
        for person_objects in original_person:
            person_objects.undraw()
        person_list1 = person(Point(630, 40), win)
        show_text_command1("you are about to enter room 2,\n click the door to enter", win)
        # button for enter target room
        while True:
            click = win.getMouse()
            if click.getX() <= 570 and click.getX() >= 430 and click.getY() <= 235 and click.getY() >= 35:
                sprint_room1()
                player_action.append('enter sprint room')
                level_history_room.append("sprint")
                break
        for person_obj1 in person_list1:
            person_obj1.undraw()
        command(win)

    # Input validation: check if the user types go east
    elif command_walk == "go east":
        # check if the user has visited the room
        if 'east' in visited_room:
            show_text_command1("you have already entered this room,\nplease try the other rooms", win)
            for person_objects in original_person:
                person_objects.undraw()
            command(win)
        visited_room.append("east")
        player_action.append('go east')
        for person_objects in original_person:
            person_objects.undraw()
        person_list2 = person(Point(900, 550), win)
        # Text(Point(275, 180), "you are about to enter the training room for legs,click the button to enter").draw(win)
        show_text_command1("you are about to enter room 3,\n click the door to enter", win)
        # button for enter target room
        while True:
            click = win.getMouse()
            if click.getX() <= 970 and click.getX() >= 830 and click.getY() <= 500 and click.getY() >= 300:
                boxing_room()
                player_action.append('enter boxing room')
                level_history_room.append("boxing")
                break
        for person_obj2 in person_list2:
            person_obj2.undraw()
        command(win)

    # Input validation: check if the user types go west
    elif command_walk == "go west":
        # check if the user has visited the room
        if 'west' in visited_room:
            show_text_command1("you have already entered this room,\nplease try the other rooms", win)
            for person_objects in original_person:
                person_objects.undraw()
            command(win)
        visited_room.append("west")
        player_action.append('go west')
        for person_objects in original_person:
            person_objects.undraw()
        person_lists3 = person(Point(100, 550), win)
        show_text_command1("you are about to enter room 4,\n click the door to enter", win)
        # button for enter target room
        while True:
            click = win.getMouse()
            if click.getX() <= 170 and click.getX() >= 30 and click.getY() <= 500 and click.getY() >= 300:
                leg_training_room()
                player_action.append('enter leg training room')
                level_history_room.append("legs")
                break
        for person_obj3 in person_lists3:
            person_obj3.undraw()
        command(win)

    # Chekc if the user has clicked the final challenge button
    elif cilck1.getX() <= 830 and cilck1.getX() >= 770 and cilck1.getY() <= 140 and cilck1.getY() >= 110:
        # check if the user has visited the room
        if "final" in visited_room:
            show_text_command1("you have already finished the final challenge", win)
            command(win)
        visited_room.append('final')
        player_action.append('enter final challenge room')
        level_history_room.append("final challenge")
        for person_objects in original_person:
            person_objects.undraw()
        final_chanllenge_room()
        command(win)

    # Error handling: if the user types wrong commands
    else:
        # Text(Point(230, 180), "oh no, you enter the wrong command, please do that again").draw(win)
        show_text_command1("oh no, you input the wrong command, \n please retry", win)
        player_action.append('wrong command')
        for person_objects in original_person:
            person_objects.undraw()
        command(win)


#create a door
def door(center,win):
    center1 = center.clone()
    center1.move(70,-100)
    center2 = center.clone()
    center2.move(-70,100)
    doorknob_center = center.clone()
    doorknob_center.move(-55,0)
    doorknob=Circle(doorknob_center,7)
    door = Rectangle(center1,center2)
    door.setFill("brown")
    door.setWidth(3)
    door.draw(win)
    doorknob.setFill("black")
    doorknob.draw(win)
    return [door,doorknob]


# create a welcome page
def main():
    global player_action
    welcome_page = GraphWin("Welcome Page", 1000, 800)
    welcome_page.setBackground("white")



    door1 = door(Point(500, 135), welcome_page)
    door2 = door(Point(100, 400), welcome_page)
    door3 = door(Point(500, 655), welcome_page)
    door4 = door(Point(900, 400), welcome_page)

    command(welcome_page)

    welcome_page.getKey()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
