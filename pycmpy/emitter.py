

import ast

# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/os/armv6.html
# http://infocenter.arm.com/help/topic/com.arm.doc.ddi0419d/DDI0419D_armv6m_arm.pdf
# http://infocenter.arm.com/help/topic/com.arm.doc.ddi0301h/DDI0301H_arm1176jzfs_r0p7_trm.pdf


class ARMv6_Emitter(ast.NodeVisitor):

    def visit_Program(self, node):
        for stmt in node.statements:
            self.visit(stmt)