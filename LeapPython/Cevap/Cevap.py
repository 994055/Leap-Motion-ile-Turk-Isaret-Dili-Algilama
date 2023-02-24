# coding=utf-8
################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, threading, time
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='leapdataset',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        print("Baglanti tamam")


    class SampleListener(Leap.Listener):
        finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
        bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

        def on_init(self, controller):
            print("Initialized")

        def on_connect(self, controller):
            print("Connected")

        def on_disconnect(self, controller):
            # Note: not dispatched when running in a debugger.
            print("Disconnected")

        def on_exit(self, controller):
            print("Exited")
        def sayisalDeger(self,degerler):
            deger = str(degerler)
            degerlen = len(deger)
            deger = deger[1:degerlen-1]
            degerDizi = deger.split(",")
            return degerDizi

        def on_frame(self, controller):
            # Get the most recent frame and report some basic information
            frame = controller.frame()

            if len(frame.hands) != 0:
                time.sleep(3)
                etiket = "6"
                print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
                      frame.id, frame.timestamp, len(frame.hands), len(frame.fingers)))

                # Get hands
                for hand in frame.hands:
                    if len(frame.hands) == 1:
                        print ("aaa")
                    if len(frame.hands) == 2:
                        handType = "Left hand" if hand.is_left else "Right hand"
                        if handType == "Right hand":
                            print("  %s, id %d, position: %s" % (
                                handType, hand.id, hand.palm_position))
                            handPosDizi=self.sayisalDeger(hand.palm_position)
                            sag_posx=float(handPosDizi[0])
                            sag_posy=float(handPosDizi[1])
                            sag_posz=float(handPosDizi[2])



                            # Get the hand's normal vector and direction
                            normal = hand.palm_normal
                            direction = hand.direction

                            # Calculate the hand's pitch, roll, and yaw angles
                            print("  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                                direction.pitch * Leap.RAD_TO_DEG,
                                normal.roll * Leap.RAD_TO_DEG,
                                direction.yaw * Leap.RAD_TO_DEG))
                            sag_pitch = direction.pitch * Leap.RAD_TO_DEG
                            sag_roll = normal.roll * Leap.RAD_TO_DEG
                            sag_yaw = direction.yaw * Leap.RAD_TO_DEG

                            # Get arm bone
                            arm = hand.arm
                            print( "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                                arm.direction,
                                arm.wrist_position,
                                arm.elbow_position))
                            armDirDizi = self.sayisalDeger(arm.direction)
                            sag_armdx=armDirDizi[0]
                            sag_armdy=armDirDizi[1]
                            sag_armdz=armDirDizi[2]
                            wristPosDizi=self.sayisalDeger(arm.wrist_position)
                            sag_wristx=wristPosDizi[0]
                            sag_wristy=wristPosDizi[1]
                            sag_wristz=wristPosDizi[2]
                            elbowPosDizi=self.sayisalDeger(arm.elbow_position)
                            sag_elbowx=elbowPosDizi[0]
                            sag_elbowy=elbowPosDizi[1]
                            sag_elbowz=elbowPosDizi[2]


                            # Get fingers
                            for finger in hand.fingers:
                                if self.finger_names[finger.type] == "Thumb":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))

                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi=self.sayisalDeger(bone.prev_joint)
                                            sag_msxThumb=thumbStartDizi[0]
                                            sag_msyThumb=thumbStartDizi[1]
                                            sag_mszThumb=thumbStartDizi[2]
                                            thumbEndDizi=self.sayisalDeger(bone.next_joint)
                                            sag_mexThumb=thumbEndDizi[0]
                                            sag_meyThumb=thumbEndDizi[1]
                                            sag_mezThumb=thumbEndDizi[2]
                                            thumbDirectionDizi=self.sayisalDeger(bone.direction)
                                            sag_mdxThumb=thumbDirectionDizi[0]
                                            sag_mdyThumb=thumbDirectionDizi[1]
                                            sag_mdzThumb=thumbDirectionDizi[2]
                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_psxThumb = thumbStartDizi[0]
                                            sag_psyThumb = thumbStartDizi[1]
                                            sag_pszThumb = thumbStartDizi[2]
                                            thumbEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_pexThumb = thumbEndDizi[0]
                                            sag_peyThumb = thumbEndDizi[1]
                                            sag_pezThumb = thumbEndDizi[2]
                                            thumbDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_pdxThumb = thumbDirectionDizi[0]
                                            sag_pdyThumb = thumbDirectionDizi[1]
                                            sag_pdzThumb = thumbDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_isxThumb = thumbStartDizi[0]
                                            sag_isyThumb = thumbStartDizi[1]
                                            sag_iszThumb = thumbStartDizi[2]
                                            thumbEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_iexThumb = thumbEndDizi[0]
                                            sag_ieyThumb = thumbEndDizi[1]
                                            sag_iezThumb = thumbEndDizi[2]
                                            thumbDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_idxThumb = thumbDirectionDizi[0]
                                            sag_idyThumb = thumbDirectionDizi[1]
                                            sag_idzThumb = thumbDirectionDizi[2]
                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_dsxThumb = thumbStartDizi[0]
                                            sag_dsyThumb = thumbStartDizi[1]
                                            sag_dszThumb = thumbStartDizi[2]
                                            thumbEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_dexThumb = thumbEndDizi[0]
                                            sag_deyThumb = thumbEndDizi[1]
                                            sag_dezThumb = thumbEndDizi[2]
                                            thumbDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_ddxThumb = thumbDirectionDizi[0]
                                            sag_ddyThumb = thumbDirectionDizi[1]
                                            sag_ddzThumb = thumbDirectionDizi[2]

                                elif self.finger_names[finger.type] == "Index":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))

                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_msxIndex = indexStartDizi[0]
                                            sag_msyIndex = indexStartDizi[1]
                                            sag_mszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_mexIndex = indexEndDizi[0]
                                            sag_meyIndex = indexEndDizi[1]
                                            sag_mezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_mdxIndex = indexDirectionDizi[0]
                                            sag_mdyIndex = indexDirectionDizi[1]
                                            sag_mdzIndex = indexDirectionDizi[2]
                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_psxIndex = indexStartDizi[0]
                                            sag_psyIndex = indexStartDizi[1]
                                            sag_pszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_pexIndex = indexEndDizi[0]
                                            sag_peyIndex = indexEndDizi[1]
                                            sag_pezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_pdxIndex = indexDirectionDizi[0]
                                            sag_pdyIndex = indexDirectionDizi[1]
                                            sag_pdzIndex = indexDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_isxIndex = indexStartDizi[0]
                                            sag_isyIndex = indexStartDizi[1]
                                            sag_iszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_iexIndex = indexEndDizi[0]
                                            sag_ieyIndex = indexEndDizi[1]
                                            sag_iezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_idxIndex = indexDirectionDizi[0]
                                            sag_idyIndex = indexDirectionDizi[1]
                                            sag_idzIndex = indexDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_dsxIndex = indexStartDizi[0]
                                            sag_dsyIndex = indexStartDizi[1]
                                            sag_dszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_dexIndex = indexEndDizi[0]
                                            sag_deyIndex = indexEndDizi[1]
                                            sag_dezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_ddxIndex = indexDirectionDizi[0]
                                            sag_ddyIndex = indexDirectionDizi[1]
                                            sag_ddzIndex = indexDirectionDizi[2]


                                elif self.finger_names[finger.type] == "Middle":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))
                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_msxMiddle = middleStartDizi[0]
                                            sag_msyMiddle = middleStartDizi[1]
                                            sag_mszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_mexMiddle = middleEndDizi[0]
                                            sag_meyMiddle = middleEndDizi[1]
                                            sag_mezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_mdxMiddle = middleDirectionDizi[0]
                                            sag_mdyMiddle = middleDirectionDizi[1]
                                            sag_mdzMiddle = middleDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_psxMiddle = middleStartDizi[0]
                                            sag_psyMiddle = middleStartDizi[1]
                                            sag_pszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_pexMiddle = middleEndDizi[0]
                                            sag_peyMiddle = middleEndDizi[1]
                                            sag_pezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_pdxMiddle = middleDirectionDizi[0]
                                            sag_pdyMiddle = middleDirectionDizi[1]
                                            sag_pdzMiddle = middleDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_isxMiddle = middleStartDizi[0]
                                            sag_isyMiddle = middleStartDizi[1]
                                            sag_iszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_iexMiddle = middleEndDizi[0]
                                            sag_ieyMiddle = middleEndDizi[1]
                                            sag_iezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_idxMiddle = middleDirectionDizi[0]
                                            sag_idyMiddle = middleDirectionDizi[1]
                                            sag_idzMiddle = middleDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_dsxMiddle = middleStartDizi[0]
                                            sag_dsyMiddle = middleStartDizi[1]
                                            sag_dszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_dexMiddle = middleEndDizi[0]
                                            sag_deyMiddle = middleEndDizi[1]
                                            sag_dezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_ddxMiddle = middleDirectionDizi[0]
                                            sag_ddyMiddle = middleDirectionDizi[1]
                                            sag_ddzMiddle = middleDirectionDizi[2]

                                elif self.finger_names[finger.type] == "Ring":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))
                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_msxRing = ringStartDizi[0]
                                            sag_msyRing = ringStartDizi[1]
                                            sag_mszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_mexRing = ringEndDizi[0]
                                            sag_meyRing = ringEndDizi[1]
                                            sag_mezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_mdxRing = ringDirectionDizi[0]
                                            sag_mdyRing = ringDirectionDizi[1]
                                            sag_mdzRing = ringDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_psxRing = ringStartDizi[0]
                                            sag_psyRing = ringStartDizi[1]
                                            sag_pszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_pexRing = ringEndDizi[0]
                                            sag_peyRing = ringEndDizi[1]
                                            sag_pezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_pdxRing = ringDirectionDizi[0]
                                            sag_pdyRing = ringDirectionDizi[1]
                                            sag_pdzRing = ringDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_isxRing = ringStartDizi[0]
                                            sag_isyRing = ringStartDizi[1]
                                            sag_iszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_iexRing = ringEndDizi[0]
                                            sag_ieyRing = ringEndDizi[1]
                                            sag_iezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_idxRing = ringDirectionDizi[0]
                                            sag_idyRing = ringDirectionDizi[1]
                                            sag_idzRing = ringDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_dsxRing = ringStartDizi[0]
                                            sag_dsyRing = ringStartDizi[1]
                                            sag_dszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_dexRing = ringEndDizi[0]
                                            sag_deyRing = ringEndDizi[1]
                                            sag_dezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_ddxRing = ringDirectionDizi[0]
                                            sag_ddyRing = ringDirectionDizi[1]
                                            sag_ddzRing = ringDirectionDizi[2]


                                elif self.finger_names[finger.type] == "Pinky":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))
                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_msxPinky = pinkyStartDizi[0]
                                            sag_msyPinky = pinkyStartDizi[1]
                                            sag_mszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_mexPinky = pinkyEndDizi[0]
                                            sag_meyPinky = pinkyEndDizi[1]
                                            sag_mezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_mdxPinky = pinkyDirectionDizi[0]
                                            sag_mdyPinky = pinkyDirectionDizi[1]
                                            sag_mdzPinky = pinkyDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_psxPinky = pinkyStartDizi[0]
                                            sag_psyPinky = pinkyStartDizi[1]
                                            sag_pszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_pexPinky = pinkyEndDizi[0]
                                            sag_peyPinky = pinkyEndDizi[1]
                                            sag_pezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_pdxPinky = pinkyDirectionDizi[0]
                                            sag_pdyPinky = pinkyDirectionDizi[1]
                                            sag_pdzPinky = pinkyDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_isxPinky = pinkyStartDizi[0]
                                            sag_isyPinky = pinkyStartDizi[1]
                                            sag_iszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_iexPinky = pinkyEndDizi[0]
                                            sag_ieyPinky = pinkyEndDizi[1]
                                            sag_iezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_idxPinky = pinkyDirectionDizi[0]
                                            sag_idyPinky = pinkyDirectionDizi[1]
                                            sag_idzPinky = pinkyDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sag_dsxPinky = pinkyStartDizi[0]
                                            sag_dsyPinky = pinkyStartDizi[1]
                                            sag_dszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sag_dexPinky = pinkyEndDizi[0]
                                            sag_deyPinky = pinkyEndDizi[1]
                                            sag_dezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sag_ddxPinky = pinkyDirectionDizi[0]
                                            sag_ddyPinky = pinkyDirectionDizi[1]
                                            sag_ddzPinky = pinkyDirectionDizi[2]
                            cursor = connection.cursor(buffered=True)
                            cursor.execute("""INSERT INTO righthand (sag_pos_x,sag_pos_y,sag_pos_z,sag_pitch,sag_roll,sag_yaw,sag_armd_x,sag_armd_y,sag_armd_z,sag_wrp_x,sag_wrp_y,sag_wrp_z,sag_elbp_x,sag_elbp_y,sag_elbp_z,sag_m_s_x_thumb,
                                            sag_m_s_y_thumb,sag_m_s_z_thumb,sag_m_e_x_thumb,sag_m_e_y_thumb,sag_m_e_z_thumb,sag_m_d_x_thumb,sag_m_d_y_thumb,sag_m_d_z_thumb,sag_p_s_x_thumb,sag_p_s_y_thumb,sag_p_s_z_thumb,sag_p_e_x_thumb,sag_p_e_y_thumb,sag_p_e_z_thumb,sag_p_d_x_thumb,sag_p_d_y_thumb,sag_p_d_z_thumb,sag_i_s_x_thumb,sag_i_s_y_thumb,sag_i_s_z_thumb,sag_i_e_x_thumb,sag_i_e_y_thumb,sag_i_e_z_thumb,sag_i_d_x_thumb,sag_i_d_y_thumb,sag_i_d_z_thumb,sag_d_s_x_thumb,sag_d_s_y_thumb,sag_d_s_z_thumb,sag_d_e_x_thumb,sag_d_e_y_thumb,sag_d_e_z_thumb,sag_d_d_x_thumb,sag_d_d_y_thumb,sag_d_d_z_thumb,sag_m_s_x_index,sag_m_s_y_index,
                                            sag_m_s_z_index,sag_m_e_x_index,sag_m_e_y_index,sag_m_e_z_index,sag_m_d_x_index,sag_m_d_y_index,sag_m_d_z_index,sag_p_s_x_index,sag_p_s_y_index,sag_p_s_z_index,sag_p_e_x_index,sag_p_e_y_index,sag_p_e_z_index,
                                            sag_p_d_x_index,sag_p_d_y_index,sag_p_d_z_index,sag_i_s_x_index,sag_i_s_y_index,sag_i_s_z_index,sag_i_e_x_index,sag_i_e_y_index,sag_i_e_z_index,sag_i_d_x_index,sag_i_d_y_index,
                                            sag_i_d_z_index,sag_d_s_x_index,sag_d_s_y_index,sag_d_s_z_index,sag_d_e_x_index,sag_d_e_y_index,sag_d_e_z_index,sag_d_d_x_index,sag_d_d_y_index,sag_d_d_z_index,sag_m_s_x_middle,sag_m_s_y_middle,sag_m_s_z_middle,sag_m_e_x_middle,sag_m_e_y_middle,sag_m_e_z_middle,sag_m_d_x_middle,sag_m_d_y_middle,sag_m_d_z_middle,sag_p_s_x_middle,sag_p_s_y_middle,sag_p_s_z_middle,sag_p_e_x_middle,sag_p_e_y_middle,sag_p_e_z_middle,sag_p_d_x_middle,sag_p_d_y_middle,sag_p_d_z_middle,sag_i_s_x_middle,sag_i_s_y_middle,sag_i_s_z_middle,sag_i_e_x_middle,sag_i_e_y_middle,sag_i_e_z_middle,sag_i_d_x_middle,sag_i_d_y_middle,sag_i_d_z_middle,sag_d_s_x_middle,
                                            sag_d_s_y_middle,sag_d_s_z_middle,sag_d_e_x_middle,sag_d_e_y_middle,sag_d_e_z_middle,sag_d_d_x_middle,sag_d_d_y_middle,sag_d_d_z_middle,sag_m_s_x_ring,sag_m_s_y_ring,sag_m_s_z_ring,sag_m_e_x_ring,sag_m_e_y_ring,sag_m_e_z_ring,sag_m_d_x_ring,sag_m_d_y_ring,sag_m_d_z_ring,sag_p_s_x_ring,sag_p_s_y_ring,sag_p_s_z_ring,sag_p_e_x_ring,sag_p_e_y_ring,sag_p_e_z_ring,sag_p_d_x_ring,sag_p_d_y_ring,sag_p_d_z_ring,sag_i_s_x_ring,sag_i_s_y_ring,sag_i_s_z_ring,sag_i_e_x_ring,sag_i_e_y_ring,sag_i_e_z_ring,sag_i_d_x_ring,sag_i_d_y_ring,sag_i_d_z_ring,sag_d_s_x_ring,sag_d_s_y_ring,sag_d_s_z_ring,
                                            sag_d_e_x_ring,sag_d_e_y_ring,sag_d_e_z_ring,sag_d_d_x_ring,sag_d_d_y_ring,sag_d_d_z_ring,sag_m_s_x_pinky,sag_m_s_y_pinky,sag_m_s_z_pinky,sag_m_e_x_pinky,sag_m_e_y_pinky,sag_m_e_z_pinky,sag_m_d_x_pinky,sag_m_d_y_pinky,sag_m_d_z_pinky,sag_p_s_x_pinky,sag_p_s_y_pinky,sag_p_s_z_pinky,sag_p_e_x_pinky,sag_p_e_y_pinky,sag_p_e_z_pinky,sag_p_d_x_pinky,sag_p_d_y_pinky,sag_p_d_z_pinky,sag_i_s_x_pinky,sag_i_s_y_pinky,sag_i_s_z_pinky,sag_i_e_x_pinky,sag_i_e_y_pinky,sag_i_e_z_pinky,sag_i_d_x_pinky,sag_i_d_y_pinky,sag_i_d_z_pinky,sag_d_s_x_pinky,sag_d_s_y_pinky,
                                            sag_d_s_z_pinky,sag_d_e_x_pinky,sag_d_e_y_pinky,sag_d_e_z_pinky,sag_d_d_x_pinky,sag_d_d_y_pinky,sag_d_d_z_pinky)
                                                                               VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
                                sag_posx, sag_posy, sag_posz, sag_pitch, sag_roll, sag_yaw, sag_armdx, sag_armdy,
                                sag_armdz, sag_wristx, sag_wristy, sag_wristz,
                                sag_elbowx, sag_elbowy, sag_elbowz, sag_msxThumb, sag_msyThumb, sag_mszThumb,
                                sag_mexThumb, sag_meyThumb, sag_mezThumb, sag_mdxThumb, sag_mdyThumb, sag_mdzThumb,
                                sag_psxThumb, sag_psyThumb,
                                sag_pszThumb, sag_pexThumb, sag_peyThumb, sag_pezThumb, sag_pdxThumb, sag_pdyThumb,
                                sag_pdzThumb,
                                sag_isxThumb, sag_isyThumb, sag_iszThumb, sag_iexThumb, sag_ieyThumb, sag_iezThumb,
                                sag_idxThumb, sag_idyThumb,
                                sag_idzThumb, sag_dsxThumb, sag_dsyThumb, sag_dszThumb, sag_dexThumb, sag_deyThumb,
                                sag_dezThumb, sag_ddxThumb,
                                sag_ddyThumb, sag_ddzThumb, sag_msxIndex, sag_msyIndex, sag_mszIndex, sag_mexIndex,
                                sag_meyIndex, sag_mezIndex,
                                sag_mdxIndex, sag_mdyIndex, sag_mdzIndex, sag_psxIndex, sag_psyIndex, sag_pszIndex,
                                sag_pexIndex, sag_peyIndex,
                                sag_pezIndex, sag_pdxIndex, sag_pdyIndex, sag_pdzIndex, sag_isxIndex, sag_isyIndex,
                                sag_iszIndex, sag_iexIndex,
                                sag_ieyIndex, sag_iezIndex, sag_idxIndex, sag_idyIndex, sag_idzIndex, sag_dsxIndex,
                                sag_dsyIndex, sag_dszIndex,
                                sag_dexIndex, sag_deyIndex, sag_dezIndex, sag_ddxIndex, sag_ddyIndex, sag_ddzIndex,
                                sag_msxMiddle, sag_msyMiddle,
                                sag_mszMiddle, sag_mexMiddle, sag_meyMiddle, sag_mezMiddle, sag_mdxMiddle,
                                sag_mdyMiddle, sag_mdzMiddle,
                                sag_psxMiddle, sag_psyMiddle, sag_pszMiddle, sag_pexMiddle, sag_peyMiddle,
                                sag_pezMiddle, sag_pdxMiddle,
                                sag_pdyMiddle, sag_pdzMiddle, sag_isxMiddle, sag_isyMiddle, sag_iszMiddle,
                                sag_iexMiddle, sag_ieyMiddle,
                                sag_iezMiddle, sag_idxMiddle, sag_idyMiddle, sag_idzMiddle, sag_dsxMiddle,
                                sag_dsyMiddle, sag_dszMiddle,
                                sag_dexMiddle, sag_deyMiddle, sag_dezMiddle, sag_ddxMiddle, sag_ddyMiddle,
                                sag_ddzMiddle, sag_msxRing, sag_msyRing,
                                sag_mszRing, sag_mexRing, sag_meyRing, sag_mezRing, sag_mdxRing, sag_mdyRing,
                                sag_mdzRing,
                                sag_psxRing, sag_psyRing, sag_pszRing, sag_pexRing, sag_peyRing, sag_pezRing,
                                sag_pdxRing,
                                sag_pdyRing, sag_pdzRing, sag_isxRing, sag_isyRing, sag_iszRing, sag_iexRing,
                                sag_ieyRing,
                                sag_iezRing, sag_idxRing, sag_idyRing, sag_idzRing, sag_dsxRing, sag_dsyRing,
                                sag_dszRing,
                                sag_dexRing, sag_deyRing, sag_dezRing, sag_ddxRing, sag_ddyRing, sag_ddzRing,
                                sag_msxPinky, sag_msyPinky,
                                sag_mszPinky, sag_mexPinky, sag_meyPinky, sag_mezPinky, sag_mdxPinky, sag_mdyPinky,
                                sag_mdzPinky,
                                sag_psxPinky, sag_psyPinky, sag_pszPinky, sag_pexPinky, sag_peyPinky, sag_pezPinky,
                                sag_pdxPinky,
                                sag_pdyPinky, sag_pdzPinky, sag_isxPinky, sag_isyPinky, sag_iszPinky, sag_iexPinky,
                                sag_ieyPinky,
                                sag_iezPinky, sag_idxPinky, sag_idyPinky, sag_idzPinky, sag_dsxPinky, sag_dsyPinky,
                                sag_dszPinky,
                                sag_dexPinky, sag_deyPinky, sag_dezPinky, sag_ddxPinky, sag_ddyPinky, sag_ddzPinky))
                            connection.commit()
                            print (cursor.rowcount, "*********Kayit Eklendi.************")
                        if handType=="Left hand":
                            print("  %s, id %d, position: %s" % (
                                handType, hand.id, hand.palm_position))
                            handPosDizi = self.sayisalDeger(hand.palm_position)
                            sol_posx = handPosDizi[0]
                            sol_posy = handPosDizi[1]
                            sol_posz = handPosDizi[2]

                            # Get the hand's normal vector and direction
                            normal = hand.palm_normal
                            direction = hand.direction

                            # Calculate the hand's pitch, roll, and yaw angles
                            print("  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                                direction.pitch * Leap.RAD_TO_DEG,
                                normal.roll * Leap.RAD_TO_DEG,
                                direction.yaw * Leap.RAD_TO_DEG))
                            sol_pitch = direction.pitch * Leap.RAD_TO_DEG
                            sol_roll = normal.roll * Leap.RAD_TO_DEG
                            sol_yaw = direction.yaw * Leap.RAD_TO_DEG

                            # Get arm bone
                            arm = hand.arm
                            print("  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                                arm.direction,
                                arm.wrist_position,
                                arm.elbow_position))
                            armDirDizi = self.sayisalDeger(arm.direction)
                            sol_armdx = armDirDizi[0]
                            sol_armdy = armDirDizi[1]
                            sol_armdz = armDirDizi[2]
                            wristPosDizi = self.sayisalDeger(arm.wrist_position)
                            sol_wristx = wristPosDizi[0]
                            sol_wristy = wristPosDizi[1]
                            sol_wristz = wristPosDizi[2]
                            elbowPosDizi = self.sayisalDeger(arm.elbow_position)
                            sol_elbowx = elbowPosDizi[0]
                            sol_elbowy = elbowPosDizi[1]
                            sol_elbowz = elbowPosDizi[2]

                            # Get fingers
                            for finger in hand.fingers:
                                if self.finger_names[finger.type] == "Thumb":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))

                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_msxThumb = thumbStartDizi[0]
                                            sol_msyThumb = thumbStartDizi[1]
                                            sol_mszThumb = thumbStartDizi[2]
                                            thumbEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_mexThumb = thumbEndDizi[0]
                                            sol_meyThumb = thumbEndDizi[1]
                                            sol_mezThumb = thumbEndDizi[2]
                                            thumbDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_mdxThumb = thumbDirectionDizi[0]
                                            sol_mdyThumb = thumbDirectionDizi[1]
                                            sol_mdzThumb = thumbDirectionDizi[2]
                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_psxThumb = thumbStartDizi[0]
                                            sol_psyThumb = thumbStartDizi[1]
                                            sol_pszThumb = thumbStartDizi[2]
                                            thumbEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_pexThumb = thumbEndDizi[0]
                                            sol_peyThumb = thumbEndDizi[1]
                                            sol_pezThumb = thumbEndDizi[2]
                                            thumbDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_pdxThumb = thumbDirectionDizi[0]
                                            sol_pdyThumb = thumbDirectionDizi[1]
                                            sol_pdzThumb = thumbDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_isxThumb = thumbStartDizi[0]
                                            sol_isyThumb = thumbStartDizi[1]
                                            sol_iszThumb = thumbStartDizi[2]
                                            thumbEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_iexThumb = thumbEndDizi[0]
                                            sol_ieyThumb = thumbEndDizi[1]
                                            sol_iezThumb = thumbEndDizi[2]
                                            thumbDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_idxThumb = thumbDirectionDizi[0]
                                            sol_idyThumb = thumbDirectionDizi[1]
                                            sol_idzThumb = thumbDirectionDizi[2]
                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            thumbStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_dsxThumb = thumbStartDizi[0]
                                            sol_dsyThumb = thumbStartDizi[1]
                                            sol_dszThumb = thumbStartDizi[2]
                                            thumbEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_dexThumb = thumbEndDizi[0]
                                            sol_deyThumb = thumbEndDizi[1]
                                            sol_dezThumb = thumbEndDizi[2]
                                            thumbDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_ddxThumb = thumbDirectionDizi[0]
                                            sol_ddyThumb = thumbDirectionDizi[1]
                                            sol_ddzThumb = thumbDirectionDizi[2]

                                elif self.finger_names[finger.type] == "Index":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))

                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_msxIndex = indexStartDizi[0]
                                            sol_msyIndex = indexStartDizi[1]
                                            sol_mszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_mexIndex = indexEndDizi[0]
                                            sol_meyIndex = indexEndDizi[1]
                                            sol_mezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_mdxIndex = indexDirectionDizi[0]
                                            sol_mdyIndex = indexDirectionDizi[1]
                                            sol_mdzIndex = indexDirectionDizi[2]
                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_psxIndex = indexStartDizi[0]
                                            sol_psyIndex = indexStartDizi[1]
                                            sol_pszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_pexIndex = indexEndDizi[0]
                                            sol_peyIndex = indexEndDizi[1]
                                            sol_pezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_pdxIndex = indexDirectionDizi[0]
                                            sol_pdyIndex = indexDirectionDizi[1]
                                            sol_pdzIndex = indexDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_isxIndex = indexStartDizi[0]
                                            sol_isyIndex = indexStartDizi[1]
                                            sol_iszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_iexIndex = indexEndDizi[0]
                                            sol_ieyIndex = indexEndDizi[1]
                                            sol_iezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_idxIndex = indexDirectionDizi[0]
                                            sol_idyIndex = indexDirectionDizi[1]
                                            sol_idzIndex = indexDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            indexStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_dsxIndex = indexStartDizi[0]
                                            sol_dsyIndex = indexStartDizi[1]
                                            sol_dszIndex = indexStartDizi[2]
                                            indexEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_dexIndex = indexEndDizi[0]
                                            sol_deyIndex = indexEndDizi[1]
                                            sol_dezIndex = indexEndDizi[2]
                                            indexDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_ddxIndex = indexDirectionDizi[0]
                                            sol_ddyIndex = indexDirectionDizi[1]
                                            sol_ddzIndex = indexDirectionDizi[2]


                                elif self.finger_names[finger.type] == "Middle":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))
                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_msxMiddle = middleStartDizi[0]
                                            sol_msyMiddle = middleStartDizi[1]
                                            sol_mszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_mexMiddle = middleEndDizi[0]
                                            sol_meyMiddle = middleEndDizi[1]
                                            sol_mezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_mdxMiddle = middleDirectionDizi[0]
                                            sol_mdyMiddle = middleDirectionDizi[1]
                                            sol_mdzMiddle = middleDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_psxMiddle = middleStartDizi[0]
                                            sol_psyMiddle = middleStartDizi[1]
                                            sol_pszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_pexMiddle = middleEndDizi[0]
                                            sol_peyMiddle = middleEndDizi[1]
                                            sol_pezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_pdxMiddle = middleDirectionDizi[0]
                                            sol_pdyMiddle = middleDirectionDizi[1]
                                            sol_pdzMiddle = middleDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_isxMiddle = middleStartDizi[0]
                                            sol_isyMiddle = middleStartDizi[1]
                                            sol_iszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_iexMiddle = middleEndDizi[0]
                                            sol_ieyMiddle = middleEndDizi[1]
                                            sol_iezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_idxMiddle = middleDirectionDizi[0]
                                            sol_idyMiddle = middleDirectionDizi[1]
                                            sol_idzMiddle = middleDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            middleStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_dsxMiddle = middleStartDizi[0]
                                            sol_dsyMiddle = middleStartDizi[1]
                                            sol_dszMiddle = middleStartDizi[2]
                                            middleEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_dexMiddle = middleEndDizi[0]
                                            sol_deyMiddle = middleEndDizi[1]
                                            sol_dezMiddle = middleEndDizi[2]
                                            middleDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_ddxMiddle = middleDirectionDizi[0]
                                            sol_ddyMiddle = middleDirectionDizi[1]
                                            sol_ddzMiddle = middleDirectionDizi[2]

                                elif self.finger_names[finger.type] == "Ring":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))
                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_msxRing = ringStartDizi[0]
                                            sol_msyRing = ringStartDizi[1]
                                            sol_mszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_mexRing = ringEndDizi[0]
                                            sol_meyRing = ringEndDizi[1]
                                            sol_mezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_mdxRing = ringDirectionDizi[0]
                                            sol_mdyRing = ringDirectionDizi[1]
                                            sol_mdzRing = ringDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_psxRing = ringStartDizi[0]
                                            sol_psyRing = ringStartDizi[1]
                                            sol_pszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_pexRing = ringEndDizi[0]
                                            sol_peyRing = ringEndDizi[1]
                                            sol_pezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_pdxRing = ringDirectionDizi[0]
                                            sol_pdyRing = ringDirectionDizi[1]
                                            sol_pdzRing = ringDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_isxRing = ringStartDizi[0]
                                            sol_isyRing = ringStartDizi[1]
                                            sol_iszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_iexRing = ringEndDizi[0]
                                            sol_ieyRing = ringEndDizi[1]
                                            sol_iezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_idxRing = ringDirectionDizi[0]
                                            sol_idyRing = ringDirectionDizi[1]
                                            sol_idzRing = ringDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            ringStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_dsxRing = ringStartDizi[0]
                                            sol_dsyRing = ringStartDizi[1]
                                            sol_dszRing = ringStartDizi[2]
                                            ringEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_dexRing = ringEndDizi[0]
                                            sol_deyRing = ringEndDizi[1]
                                            sol_dezRing = ringEndDizi[2]
                                            ringDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_ddxRing = ringDirectionDizi[0]
                                            sol_ddyRing = ringDirectionDizi[1]
                                            sol_ddzRing = ringDirectionDizi[2]


                                elif self.finger_names[finger.type] == "Pinky":
                                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                                        self.finger_names[finger.type],
                                        finger.id,
                                        finger.length,
                                        finger.width))
                                    # Get bones
                                    for b in range(0, 4):
                                        bone = finger.bone(b)
                                        if self.bone_names[bone.type] == "Metacarpal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_msxPinky = pinkyStartDizi[0]
                                            sol_msyPinky = pinkyStartDizi[1]
                                            sol_mszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_mexPinky = pinkyEndDizi[0]
                                            sol_meyPinky = pinkyEndDizi[1]
                                            sol_mezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_mdxPinky = pinkyDirectionDizi[0]
                                            sol_mdyPinky = pinkyDirectionDizi[1]
                                            sol_mdzPinky = pinkyDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Proximal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_psxPinky = pinkyStartDizi[0]
                                            sol_psyPinky = pinkyStartDizi[1]
                                            sol_pszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_pexPinky = pinkyEndDizi[0]
                                            sol_peyPinky = pinkyEndDizi[1]
                                            sol_pezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_pdxPinky = pinkyDirectionDizi[0]
                                            sol_pdyPinky = pinkyDirectionDizi[1]
                                            sol_pdzPinky = pinkyDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Intermediate":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_isxPinky = pinkyStartDizi[0]
                                            sol_isyPinky = pinkyStartDizi[1]
                                            sol_iszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_iexPinky = pinkyEndDizi[0]
                                            sol_ieyPinky = pinkyEndDizi[1]
                                            sol_iezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_idxPinky = pinkyDirectionDizi[0]
                                            sol_idyPinky = pinkyDirectionDizi[1]
                                            sol_idzPinky = pinkyDirectionDizi[2]

                                        elif self.bone_names[bone.type] == "Distal":
                                            print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                                                self.bone_names[bone.type],
                                                bone.prev_joint,
                                                bone.next_joint,
                                                bone.direction))
                                            pinkyStartDizi = self.sayisalDeger(bone.prev_joint)
                                            sol_dsxPinky = pinkyStartDizi[0]
                                            sol_dsyPinky = pinkyStartDizi[1]
                                            sol_dszPinky = pinkyStartDizi[2]
                                            pinkyEndDizi = self.sayisalDeger(bone.next_joint)
                                            sol_dexPinky = pinkyEndDizi[0]
                                            sol_deyPinky = pinkyEndDizi[1]
                                            sol_dezPinky = pinkyEndDizi[2]
                                            pinkyDirectionDizi = self.sayisalDeger(bone.direction)
                                            sol_ddxPinky = pinkyDirectionDizi[0]
                                            sol_ddyPinky = pinkyDirectionDizi[1]
                                            sol_ddzPinky = pinkyDirectionDizi[2]
                            cursor = connection.cursor(buffered=True)
                            cursor.execute("""INSERT INTO lefthand (sol_pos_x,sol_pos_y,sol_pos_z,sol_pitch,sol_roll,sol_yaw,sol_armd_x,sol_armd_y,sol_armd_z,sol_wrp_x,sol_wrp_y,sol_wrp_z,sol_elbp_x,sol_elbp_y,sol_elbp_z,sol_m_s_x_thumb,
                                            sol_m_s_y_thumb,sol_m_s_z_thumb,sol_m_e_x_thumb,sol_m_e_y_thumb,sol_m_e_z_thumb,sol_m_d_x_thumb,sol_m_d_y_thumb,sol_m_d_z_thumb,sol_p_s_x_thumb,sol_p_s_y_thumb,sol_p_s_z_thumb,sol_p_e_x_thumb,sol_p_e_y_thumb,sol_p_e_z_thumb,sol_p_d_x_thumb,sol_p_d_y_thumb,sol_p_d_z_thumb,sol_i_s_x_thumb,sol_i_s_y_thumb,sol_i_s_z_thumb,sol_i_e_x_thumb,sol_i_e_y_thumb,sol_i_e_z_thumb,sol_i_d_x_thumb,sol_i_d_y_thumb,sol_i_d_z_thumb,sol_d_s_x_thumb,sol_d_s_y_thumb,sol_d_s_z_thumb,sol_d_e_x_thumb,sol_d_e_y_thumb,sol_d_e_z_thumb,sol_d_d_x_thumb,sol_d_d_y_thumb,sol_d_d_z_thumb,sol_m_s_x_index,sol_m_s_y_index,
                                            sol_m_s_z_index,sol_m_e_x_index,sol_m_e_y_index,sol_m_e_z_index,sol_m_d_x_index,sol_m_d_y_index,sol_m_d_z_index,sol_p_s_x_index,sol_p_s_y_index,sol_p_s_z_index,sol_p_e_x_index,sol_p_e_y_index,sol_p_e_z_index,
                                            sol_p_d_x_index,sol_p_d_y_index,sol_p_d_z_index,sol_i_s_x_index,sol_i_s_y_index,sol_i_s_z_index,sol_i_e_x_index,sol_i_e_y_index,sol_i_e_z_index,sol_i_d_x_index,sol_i_d_y_index,
                                            sol_i_d_z_index,sol_d_s_x_index,sol_d_s_y_index,sol_d_s_z_index,sol_d_e_x_index,sol_d_e_y_index,sol_d_e_z_index,sol_d_d_x_index,sol_d_d_y_index,sol_d_d_z_index,sol_m_s_x_middle,sol_m_s_y_middle,sol_m_s_z_middle,sol_m_e_x_middle,sol_m_e_y_middle,sol_m_e_z_middle,sol_m_d_x_middle,sol_m_d_y_middle,sol_m_d_z_middle,sol_p_s_x_middle,sol_p_s_y_middle,sol_p_s_z_middle,sol_p_e_x_middle,sol_p_e_y_middle,sol_p_e_z_middle,sol_p_d_x_middle,sol_p_d_y_middle,sol_p_d_z_middle,sol_i_s_x_middle,sol_i_s_y_middle,sol_i_s_z_middle,sol_i_e_x_middle,sol_i_e_y_middle,sol_i_e_z_middle,sol_i_d_x_middle,sol_i_d_y_middle,sol_i_d_z_middle,sol_d_s_x_middle,
                                            sol_d_s_y_middle,sol_d_s_z_middle,sol_d_e_x_middle,sol_d_e_y_middle,sol_d_e_z_middle,sol_d_d_x_middle,sol_d_d_y_middle,sol_d_d_z_middle,sol_m_s_x_ring,sol_m_s_y_ring,sol_m_s_z_ring,sol_m_e_x_ring,sol_m_e_y_ring,sol_m_e_z_ring,sol_m_d_x_ring,sol_m_d_y_ring,sol_m_d_z_ring,sol_p_s_x_ring,sol_p_s_y_ring,sol_p_s_z_ring,sol_p_e_x_ring,sol_p_e_y_ring,sol_p_e_z_ring,sol_p_d_x_ring,sol_p_d_y_ring,sol_p_d_z_ring,sol_i_s_x_ring,sol_i_s_y_ring,sol_i_s_z_ring,sol_i_e_x_ring,sol_i_e_y_ring,sol_i_e_z_ring,sol_i_d_x_ring,sol_i_d_y_ring,sol_i_d_z_ring,sol_d_s_x_ring,sol_d_s_y_ring,sol_d_s_z_ring,
                                            sol_d_e_x_ring,sol_d_e_y_ring,sol_d_e_z_ring,sol_d_d_x_ring,sol_d_d_y_ring,sol_d_d_z_ring,sol_m_s_x_pinky,sol_m_s_y_pinky,sol_m_s_z_pinky,sol_m_e_x_pinky,sol_m_e_y_pinky,sol_m_e_z_pinky,sol_m_d_x_pinky,sol_m_d_y_pinky,sol_m_d_z_pinky,sol_p_s_x_pinky,sol_p_s_y_pinky,sol_p_s_z_pinky,sol_p_e_x_pinky,sol_p_e_y_pinky,sol_p_e_z_pinky,sol_p_d_x_pinky,sol_p_d_y_pinky,sol_p_d_z_pinky,sol_i_s_x_pinky,sol_i_s_y_pinky,sol_i_s_z_pinky,sol_i_e_x_pinky,sol_i_e_y_pinky,sol_i_e_z_pinky,sol_i_d_x_pinky,sol_i_d_y_pinky,sol_i_d_z_pinky,sol_d_s_x_pinky,sol_d_s_y_pinky,
                                            sol_d_s_z_pinky,sol_d_e_x_pinky,sol_d_e_y_pinky,sol_d_e_z_pinky,sol_d_d_x_pinky,sol_d_d_y_pinky,sol_d_d_z_pinky)
                                                                               VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
                                sol_posx, sol_posy, sol_posz, sol_pitch, sol_roll, sol_yaw, sol_armdx, sol_armdy,
                                sol_armdz, sol_wristx, sol_wristy, sol_wristz,
                                sol_elbowx, sol_elbowy, sol_elbowz, sol_msxThumb, sol_msyThumb, sol_mszThumb,
                                sol_mexThumb, sol_meyThumb, sol_mezThumb, sol_mdxThumb, sol_mdyThumb, sol_mdzThumb,
                                sol_psxThumb, sol_psyThumb,
                                sol_pszThumb, sol_pexThumb, sol_peyThumb, sol_pezThumb, sol_pdxThumb, sol_pdyThumb,
                                sol_pdzThumb,
                                sol_isxThumb, sol_isyThumb, sol_iszThumb, sol_iexThumb, sol_ieyThumb, sol_iezThumb,
                                sol_idxThumb, sol_idyThumb,
                                sol_idzThumb, sol_dsxThumb, sol_dsyThumb, sol_dszThumb, sol_dexThumb, sol_deyThumb,
                                sol_dezThumb, sol_ddxThumb,
                                sol_ddyThumb, sol_ddzThumb, sol_msxIndex, sol_msyIndex, sol_mszIndex, sol_mexIndex,
                                sol_meyIndex, sol_mezIndex,
                                sol_mdxIndex, sol_mdyIndex, sol_mdzIndex, sol_psxIndex, sol_psyIndex, sol_pszIndex,
                                sol_pexIndex, sol_peyIndex,
                                sol_pezIndex, sol_pdxIndex, sol_pdyIndex, sol_pdzIndex, sol_isxIndex, sol_isyIndex,
                                sol_iszIndex, sol_iexIndex,
                                sol_ieyIndex, sol_iezIndex, sol_idxIndex, sol_idyIndex, sol_idzIndex, sol_dsxIndex,
                                sol_dsyIndex, sol_dszIndex,
                                sol_dexIndex, sol_deyIndex, sol_dezIndex, sol_ddxIndex, sol_ddyIndex, sol_ddzIndex,
                                sol_msxMiddle, sol_msyMiddle,
                                sol_mszMiddle, sol_mexMiddle, sol_meyMiddle, sol_mezMiddle, sol_mdxMiddle,
                                sol_mdyMiddle, sol_mdzMiddle,
                                sol_psxMiddle, sol_psyMiddle, sol_pszMiddle, sol_pexMiddle, sol_peyMiddle,
                                sol_pezMiddle, sol_pdxMiddle,
                                sol_pdyMiddle, sol_pdzMiddle, sol_isxMiddle, sol_isyMiddle, sol_iszMiddle,
                                sol_iexMiddle, sol_ieyMiddle,
                                sol_iezMiddle, sol_idxMiddle, sol_idyMiddle, sol_idzMiddle, sol_dsxMiddle,
                                sol_dsyMiddle, sol_dszMiddle,
                                sol_dexMiddle, sol_deyMiddle, sol_dezMiddle, sol_ddxMiddle, sol_ddyMiddle,
                                sol_ddzMiddle, sol_msxRing, sol_msyRing,
                                sol_mszRing, sol_mexRing, sol_meyRing, sol_mezRing, sol_mdxRing, sol_mdyRing,
                                sol_mdzRing,
                                sol_psxRing, sol_psyRing, sol_pszRing, sol_pexRing, sol_peyRing, sol_pezRing,
                                sol_pdxRing,
                                sol_pdyRing, sol_pdzRing, sol_isxRing, sol_isyRing, sol_iszRing, sol_iexRing,
                                sol_ieyRing,
                                sol_iezRing, sol_idxRing, sol_idyRing, sol_idzRing, sol_dsxRing, sol_dsyRing,
                                sol_dszRing,
                                sol_dexRing, sol_deyRing, sol_dezRing, sol_ddxRing, sol_ddyRing, sol_ddzRing,
                                sol_msxPinky, sol_msyPinky,
                                sol_mszPinky, sol_mexPinky, sol_meyPinky, sol_mezPinky, sol_mdxPinky, sol_mdyPinky,
                                sol_mdzPinky,
                                sol_psxPinky, sol_psyPinky, sol_pszPinky, sol_pexPinky, sol_peyPinky, sol_pezPinky,
                                sol_pdxPinky,
                                sol_pdyPinky, sol_pdzPinky, sol_isxPinky, sol_isyPinky, sol_iszPinky, sol_iexPinky,
                                sol_ieyPinky,
                                sol_iezPinky, sol_idxPinky, sol_idyPinky, sol_idzPinky, sol_dsxPinky, sol_dsyPinky,
                                sol_dszPinky,
                                sol_dexPinky, sol_deyPinky, sol_dezPinky, sol_ddxPinky, sol_ddyPinky, sol_ddzPinky))
                            connection.commit()
                            print (cursor.rowcount, "*********Kayit Eklendi.************")


    def main():
        # Create a sample listener and controller
        listener = SampleListener()
        controller = Leap.Controller()

        # Have the sample listener receive events from the controller
        controller.add_listener(listener)

        # Keep this process running until Enter is pressed
        print("Press Enter to quit...")
        try:
            sys.stdin.readline()
        except KeyboardInterrupt:
            pass
        finally:
            # Remove the sample listener when done
            controller.remove_listener(listener)


    if __name__ == "__main__":
        main()
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
   print ""