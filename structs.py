import struct


class Vec2:
    fmt = "ff"
    size = struct.calcsize(fmt)

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.x}, {self.y}>"

    def pack(self, buffer: bytearray, offset: int) -> int:
        struct.pack_into(Vec2.fmt, buffer, offset, self.x, self.y)
        return offset + Vec2.size


class Vec3:
    fmt = "fff"
    size = struct.calcsize(fmt)

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def pack(self, buffer: bytearray, offset: int) -> int:
        struct.pack_into(Vec3.fmt, buffer, offset, self.x, self.y, self.z)
        return offset + Vec3.size


class Vertex:
    size = Vec3.size + Vec3.size + Vec2.size

    def __init__(self, raw_vertex: list[float]):
        assert (len(raw_vertex) == 8)
        # T2F_N3F_V3F
        self.texCoord = Vec2(raw_vertex[0], raw_vertex[1])
        self.normal = Vec3(raw_vertex[2], raw_vertex[3], raw_vertex[4])
        self.position = Vec3(raw_vertex[5], raw_vertex[6], raw_vertex[7])

    def __repr__(self):
        return f"Vertex({self.position}, {self.normal}, {self.texCoord})"

    def pack(self, buffer: bytearray, offset: int) -> int:
        offset = self.position.pack(buffer, offset)
        offset = self.normal.pack(buffer, offset)
        offset = self.texCoord.pack(buffer, offset)
        return offset
