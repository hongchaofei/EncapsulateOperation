# -*- coding: utf-8 -*-
"""
Created on 2021/7/8
@project: EncapsulateOperation
@filename: Simulator
@author: Hong Chaofei
@contact: hongchf@gmail.com

@description: 
"""
import torch
import tensorflow
tensorflow.Tensor
from Variable import Variable
from typing import List

class Simulator(object):

    def __init__(self):
        super(Simulator, self).__init__()
        self.operations = list()
        self.varibles = dict()
        self.temp_dict = dict()
        self.update_dict = dict()
        self.basic_operation = dict()


    def add_variables(self, vars: List[Variable]):

        if isinstance(vars, Variable):
            #单个变量的情况
            assert vars.name is not None

            self.varibles[vars.name] = vars
            vars.backend_variable_dict = self.varibles
        else:
            assert isinstance(vars, list)
            # 多个变量的情况
            for var in vars:
                assert isinstance(var, Variable)
                assert var.name is not None
                self.varibles[var.name] = var
                var.backend_variable_dict = self.varibles


    def extract_op(self, op_code):
        extracted_ops = []
        assert op_code[0] in self.basic_operation
        this_code = [op_code[0]]
        for var in op_code[1:]:
            assert isinstance(var, Variable)
            if '[tmpVar]' in var.name and var.name not in self.temp_dict:
                assert var.op_code is not None
                extracted_ops.extend(self.extract_op(var.op_code))
                self.temp_dict[var.name] = var
            this_code.append(var.name)
        extracted_ops.append(this_code)
        return extracted_ops



    def add_operations(self, return_var_names, op, input_var_names):

        input_vars = []
        for input_name in input_var_names:
            input_vars.append(self.varibles[input_name])

        outputs = op(*input_vars)

        for output_var, target_var_name in zip(outputs, return_var_names):
            # 就不把Variable进行到底了，先做一个过渡方案，在真正计算前都转化为原来的后端变量吧
            self.update_dict[target_var_name.name] = output_var.name
            assert output_var.op_code is not None
            self.operations.extend(self.extract_op(output_var.op_code))













