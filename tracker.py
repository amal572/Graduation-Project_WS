import numpy as np

class Tracker(object):
    def __init__(self, dist_thresh=50, max_humans=6):
        self._dist_thresh = dist_thresh
        self._max_humans = max_humans

        self._dict_id2skeleton = {}
        self._cnt_humans = 0

    def track(self, curr_skels):
        N = len(curr_skels)

        if len(self._dict_id2skeleton) > 0:
            ids, prev_skels = map(list, zip(*self._dict_id2skeleton.items()))
            good_matches = self._match_features(prev_skels, curr_skels)

            self._dict_id2skeleton = {}
            is_matched = [False] * N
            for i2, i1 in good_matches.items():
                human_id = ids[i1]
                self._dict_id2skeleton[human_id] = np.array(curr_skels[i2])
                is_matched[i2] = True
            unmatched_idx = [i for i, matched in enumerate(
                is_matched) if not matched]
        else:
            good_matches = []
            unmatched_idx = range(N)

        num_humans_to_add = min(len(unmatched_idx), self._max_humans - len(good_matches))
        for i in range(num_humans_to_add):
            self._cnt_humans += 1
            self._dict_id2skeleton[self._cnt_humans] = np.array(curr_skels[unmatched_idx[i]])
        return self._dict_id2skeleton

    def _get_neck(self, skeleton):
        x, y = skeleton[2], skeleton[3]
        return x, y

    def _match_features(self, features1, features2):
        features1, features2 = np.array(features1), np.array(features2)

        cost = lambda x1, x2: np.linalg.norm(x1 - x2)

        def calc_dist(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

        def cost(sk1, sk2):
            joints = np.array([0, 1, 2])
            sk1, sk2 = sk1[joints], sk2[joints]
            valid_idx = np.logical_and(sk1 != 0, sk2 != 0)
            sk1, sk2 = sk1[valid_idx], sk2[valid_idx]
            sum_dist, num_points = 0, int(len(sk1) / 2)
            if num_points == 0:
                return 99999
            else:
                for i in range(num_points):
                    idx = i * 2
                    sum_dist += calc_dist(sk1[idx:idx + 2], sk2[idx:idx + 2])
                mean_dist = sum_dist / num_points
                mean_dist /= (1.0 + 0.05 * num_points)
                return mean_dist

        good_matches = {}
        n1, n2 = len(features1), len(features2)
        if n1 and n2:
            dist_matrix = [[cost(f1, f2) for f2 in features2]
                           for f1 in features1]
            dist_matrix = np.array(dist_matrix)
            matches_f1_to_f2 = [dist_matrix[row, :].argmin() for row in range(n1)]

            matches_f2_to_f1 = [dist_matrix[:, col].argmin() for col in range(n2)]

            for i1, i2 in enumerate(matches_f1_to_f2):
                if matches_f2_to_f1[i2] == i1 and dist_matrix[i1, i2] < self._dist_thresh:
                    good_matches[i2] = i1

        return good_matches
