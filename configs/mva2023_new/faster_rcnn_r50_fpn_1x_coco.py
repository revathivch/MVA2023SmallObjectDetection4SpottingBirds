_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    './drone_dataset.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
