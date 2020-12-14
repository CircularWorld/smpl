下载 [model.zip](https://github.com/YunYang1994/smplify/releases/tag/v1.0) 并解压至 `code` 目录下：

## 运行 smpl

```bashrc
$ python hello_smpl.py
$ python render_smpl.py
```

## 运行 smplify

```bashrc
$ python fit_3d.py
```


|index     |  joint name      |    corresponding SMPL joint ids   |
|----------|:----------------:|---------------------------------:|
| 0        |  Right ankle     |8                                  |
| 1        |  Right knee      |5                                  |
| 2        |  Right hip       |2                                  |
| 3        |  Left hip        |1                                  |
| 4        |  Left knee       |4                                  |
| 5        |  Left ankle      |7                                  |
| 6        |  Right wrist     |21                                 |
| 7        |  Right elbow     |19                                 |
| 8        |  Right shoulder  |17                                 |
| 9        |  Left shoulder   |16                                 |
| 10       |  Left elbow      |18                                 |
| 11       |  Left wrist      |20                                 |
| 12       |  Neck            |-                                  |
| 13       |  Head top        |vertex 411 (see line 233:fit_3d.py)|

