#!/usr/bin/env python2

kNsToEstFnMapping = {'traj_est': 'stamped_traj_estimate',
                     'pose_graph': 'stamped_pose_graph_estimate',
                     'ba_estimate': 'stamped_ba_estimate'}
kNsToGtFnMapping = {'traj_est': 'stamped_groundtruth',
                     'pose_graph': 'stamped_pose_graph_gt',
                     'ba_estimate': 'stamped_ba_gt'}
kNsToMatchFnMapping = {'traj_est': 'stamped_est_gt_matches',
                       'pose_graph': 'stamped_pg_gt_matches',
                       'ba_estimate': 'stamped_ba_gt_matches'}
kFnExt = 'txt'
