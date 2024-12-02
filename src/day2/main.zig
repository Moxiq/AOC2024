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
    const a = try io.read_input_trimmed(allocator, input_file);
    defer allocator.free(a);

    var safe_levels: i32 = 0;
    var iter = std.mem.splitAny(u8, a, "\n");
    report: while (iter.next()) |entry| {
        var lvl_list = try std.ArrayList(i32).initCapacity(allocator, 10);
        defer lvl_list.deinit();
        var lvls = std.mem.splitAny(u8, entry, " ");
        while (lvls.next()) |lvl| {
            const num: i32 = try std.fmt.parseInt(i32, lvl, 10);

            if (lvl_list.items.len == 0) {
                try lvl_list.append(num);
                continue;
            }

            const diff = @abs(num - lvl_list.getLast());
            if (diff < 1 or diff > 3) {
                continue :report;
            }

            try lvl_list.append(num);

            // Check inc/dec
            if (lvl_list.items.len >= 3) {
                const len: usize = lvl_list.items.len;
                if ((lvl_list.items[len - 3] > lvl_list.items[len - 2]) and (lvl_list.items[len - 2] < lvl_list.items[len - 1])) {
                    continue :report;
                }
                if ((lvl_list.items[len - 3] < lvl_list.items[len - 2]) and (lvl_list.items[len - 2] > lvl_list.items[len - 1])) {
                    continue :report;
                }
            }
        }

        safe_levels += 1;
    }

    return safe_levels;
}

pub fn p2(allocator: std.mem.Allocator, input_file: []const u8) !i32 {
    const a = try io.read_input_trimmed(allocator, input_file);
    defer allocator.free(a);

    var safe_levels: i32 = 0;
    var iter = std.mem.splitAny(u8, a, "\n");
    while (iter.next()) |entry| {
        var lvl_list = try std.ArrayList(i32).initCapacity(allocator, 10);
        defer lvl_list.deinit();
        var lvls = std.mem.splitAny(u8, entry, " ");
        while (lvls.next()) |lvl| {
            const num: i32 = try std.fmt.parseInt(i32, lvl, 10);

            try lvl_list.append(num);
        }
        if (try check_ign(&lvl_list, false)) {
            safe_levels += 1;
        }
    }

    return safe_levels;
}

pub fn check_ign(lvl_list: *const std.ArrayList(i32), ign: bool) !bool {
    for (lvl_list.items, 0..lvl_list.items.len) |lvl, i| {
        if (i == 0) continue;

        const diff = @abs(lvl - lvl_list.items[i - 1]);
        if (diff < 1 or diff > 3) {
            if (ign) return false;
            var ign_list = try lvl_list.clone();
            defer ign_list.deinit();
            _ = ign_list.orderedRemove(i);
            return check_ign(&ign_list, true);
        }

        // Check inc/dec
        if (i >= 2) {
            if ((lvl_list.items[i - 2] > lvl_list.items[i - 1]) and (lvl_list.items[i - 1] < lvl_list.items[i])) {
                if (ign) return false;
                var ign_list = try lvl_list.clone();
                defer ign_list.deinit();
                _ = ign_list.orderedRemove(i);
                return check_ign(&ign_list, true);
            }
            if ((lvl_list.items[i - 2] < lvl_list.items[i - 1]) and (lvl_list.items[i - 1] > lvl_list.items[i])) {
                if (ign) return false;
                var ign_list = try lvl_list.clone();
                defer ign_list.deinit();
                _ = ign_list.orderedRemove(i);
                return check_ign(&ign_list, true);
            }
        }
    }

    return true;
}
