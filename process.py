import struct
from pywavefront import Wavefront
from pywavefront.mesh import Mesh
from pywavefront.material import Material
from structs import Vertex


def reshape_vertices(raw_vertices: list[float]):
    num_vertices = len(raw_vertices) // 8
    print(f"{num_vertices} vertices")
    vertices = [Vertex(raw_vertices[i * 8: (i + 1) * 8]) for i in range(num_vertices)]
    return vertices


def process_mesh(name: str, mesh: Mesh) -> list[Vertex]:
    print(f"Processing mesh {name}")
    material: Material = mesh.materials[0]
    assert (material.is_default)
    assert (material.vertex_format == "T2F_N3F_V3F")
    vertices = reshape_vertices(material.vertices)
    return vertices


def write_mesh(filename: str, vertices: list[Vertex]):
    # see format.hexpat for the binary format
    num_vertices = len(vertices)
    header_fmt = "I"
    header_size = struct.calcsize(header_fmt)
    buffer = bytearray(header_size + num_vertices * Vertex.size)

    struct.pack_into(header_fmt, buffer, 0, num_vertices)
    offset = header_size
    for vertex in vertices:
        offset = vertex.pack(buffer, offset)

    with open(filename, "wb") as f:
        print(f"Writing mesh {filename}")
        f.write(buffer)


def process_file(filename: str):
    scene = Wavefront(filename)
    for name, mesh in scene.meshes.items():
        vertices = process_mesh(name, mesh)
        write_mesh(f"output/{name}.mesh", vertices)
