struct Vec2 {
	float x;
	float y;
};
struct Vec3 {
	float x;
	float y;
	float z;
};
struct Vertex {
	Vec3 position;
	Vec3 normal;
	Vec2 texCoord;
};
u32 numVertices @0x00;
Vertex vertices[numVertices] @0x04;
