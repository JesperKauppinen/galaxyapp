def transform(self, x, y):
    # return self.transform_2D(x, y)
    return self.transform_perspective(x, y)


def transform_2D(self, x, y):
    return x, y


def transform_perspective(self, x, y):
    lin_y = y / self.height * self.perspective_points_y
    if lin_y > self.perspective_points_y:
        lin_y = self.perspective_points_y

    diff_x = x - self.perspective_points_x
    diff_y = self.perspective_points_y - lin_y
    factor_y = diff_y / self.perspective_points_y
    factor_y = pow(factor_y, 3)

    tr_x = self.perspective_points_x + diff_x * factor_y
    tr_y = self.perspective_points_y - factor_y * self.perspective_points_y
    return int(tr_x), int(tr_y)
