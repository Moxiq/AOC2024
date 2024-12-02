const std = @import("std");
const io = @import("io");

const stdout = std.io.getStdOut().writer();

pub fn main() !void {
    // const stdout = std.io.getStdOut().writer();
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const dir_path = comptime std.fs.path.dirname(@src().file) orelse ".";
    const input_file = dir_path ++ "/" ++ "input.txt";

    try stdout.print("{s}\n", .{dir_path});
    try stdout.print("p1: {}\n", .{try p1(allocator, input_file)});
    try stdout.print("p2: {}\n", .{try p2(allocator, input_file)});
    try stdout.print("---------------------------\n", .{});
}

pub fn p1(allocator: std.mem.Allocator, input_file: []const u8) !i32 {
    const a = try io.read_input(allocator, input_file);
    defer allocator.free(a);
    var l1 = std.ArrayList(i32).init(allocator);
    var l2 = std.ArrayList(i32).init(allocator);
    defer l1.deinit();
    defer l2.deinit();

    var i: u32 = 0;
    var it = std.mem.splitAny(u8, a, "\n \t");
    while (it.next()) |e| : (i += 1) {
        if (e.len == 0) continue;
        if (i % 2 == 0) {
            try l1.append(try std.fmt.parseInt(i32, e, 10));
        } else {
            try l2.append(try std.fmt.parseInt(i32, e, 10));
        }
    }

    std.mem.sort(i32, l1.items, {}, comptime std.sort.asc(i32));
    std.mem.sort(i32, l2.items, {}, comptime std.sort.asc(i32));

    var sum: i32 = 0;
    for (l1.items, l2.items) |f, s| {
        sum += @intCast(@abs(f - s));
    }

    return sum;
}

pub fn p2(allocator: std.mem.Allocator, input_file: []const u8) !i32 {
    const a = try io.read_input(allocator, input_file);
    defer allocator.free(a);
    var l1 = std.ArrayList(i32).init(allocator);
    var l2 = std.ArrayList(i32).init(allocator);
    defer l1.deinit();
    defer l2.deinit();

    var i: u32 = 0;
    var it = std.mem.splitAny(u8, a, "\n \t");
    while (it.next()) |e| : (i += 1) {
        if (e.len == 0) continue;
        if (i % 2 == 0) {
            try l1.append(try std.fmt.parseInt(i32, e, 10));
        } else {
            try l2.append(try std.fmt.parseInt(i32, e, 10));
        }
    }

    var sum: i32 = 0;
    for (l1.items) |left| {
        var counts: i32 = 0;
        for (l2.items) |right| {
            if (left == right) counts += 1;
        }
        sum += left * counts;
    }

    return sum;
}
