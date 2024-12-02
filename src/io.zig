const std = @import("std");

pub fn read_input(allocator: std.mem.Allocator, path: []const u8) ![]u8 {
    return try std.fs.cwd().readFileAlloc(allocator, path, std.math.maxInt(u32));
}

pub fn read_input_trimmed(allocator: std.mem.Allocator, path: []const u8) ![]const u8 {
    const inp = try std.fs.cwd().readFileAlloc(allocator, path, std.math.maxInt(u32));
    defer allocator.free(inp);
    const trimmed = std.mem.trimRight(u8, inp, "\n");
    return try allocator.dupe(u8, trimmed);
}

test "test" {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    const s = try read_input(allocator, "test.txt");
    std.debug.print("{s}\n", .{s});
}
