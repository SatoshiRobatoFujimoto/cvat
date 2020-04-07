# Copyright (C) 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

from rest_framework import serializers


class DatasetFormatSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64, source='DISPLAY_NAME')
    tag = serializers.CharField(max_length=64, source='TAG')
    ext = serializers.CharField(max_length=64, source='EXT')
    version = serializers.CharField(max_length=64, source='VERSION')