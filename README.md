代码来自 [SMPL](https://smpl.is.tue.mpg.de/) 和 [SMPLify](http://smplify.is.tue.mpg.de/) 官网, 经过源码修改, 可直接运行. 首先下载 [model.zip](https://github.com/YunYang1994/smplify/releases/tag/v1.0) 并解压至 `code` 目录下, 然后进入 `code` 目录：

```bashrc
$ sudo apt-get install libosmesa6-dev
$ pip3 install opendr==0.78
$ pip3 install pyrender trimesh
```

## 运行 smpl

```bashrc
$ python hello_smpl.py
```

## 运行 smplify

```bashrc
$ python fit_3d.py
```

## 相关文档

- [视频人体动作捕捉技术](https://zhuanlan.zhihu.com/p/208669724)
- [SMPL: A Skinned Multi-Person Linear Model - GitHub](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwixx93f1u_tAhVB-2EKHeANBkQQFjAIegQIChAC&url=https%3A%2F%2Fraw.githubusercontent.com%2FEros-L%2FEros-L.github.io%2Fmaster%2F_posts%2Fthesis%2Fweek9%2FSMPL-document.pdf&usg=AOvVaw3EBFl-UTOuxBTRvZmX0VlG)
