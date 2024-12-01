const std = @import("std");
const builtin = @import("builtin");
const fs = std.fs;
const mem = std.mem;
const process = std.process;
// Although this function looks imperative, note that its job is to
// declaratively construct a build graph that will be executed by an external
// runner.
pub fn build(b: *std.Build) !void {
    // Standard target options allows the person running `zig build` to choose
    // what target to build for. Here we do not override the defaults, which
    // means any target is allowed, and the default is native. Other options
    // for restricting supported target set are available.
    const target = b.standardTargetOptions(.{});

    // Standard optimization options allow the person running `zig build` to select
    // between Debug, ReleaseSafe, ReleaseFast, and ReleaseSmall. Here we do not
    // set a preferred release mode, allowing the user to decide how to optimize.
    const optimize = b.standardOptimizeOption(.{});

    // Read all .zig files from src/myfolder
    var src_dir = try fs.cwd().openDir("src/d1", .{ .iterate = true });
    defer src_dir.close();

    var walker = try src_dir.walk(b.allocator);
    defer walker.deinit();

    while (try walker.next()) |entry| {
        // Only process .zig files
        if (entry.kind != .file or !mem.endsWith(u8, entry.path, ".zig")) continue;

        // Create an executable for each .zig file
        const full_path = try std.fmt.allocPrint(b.allocator, "src/d1/{s}", .{entry.path});
        const exe = b.addExecutable(.{
            .name = try std.fmt.allocPrint(b.allocator, "exe_{s}", .{std.fs.path.stem(entry.path)}),
            .root_source_file = b.path(full_path),
            .target = target,
            .optimize = optimize,
        });

        // Add a run step for this executable
        const run_cmd = b.addRunArtifact(exe);
        run_cmd.step.dependOn(b.getInstallStep());
        if (b.args) |args| {
            run_cmd.addArgs(args);
        }

        const run_step = b.step(try std.fmt.allocPrint(b.allocator, "run-{s}", .{std.fs.path.stem(entry.path)}), try std.fmt.allocPrint(b.allocator, "Run the {s} executable", .{entry.path}));
        run_step.dependOn(&run_cmd.step);

        // Automatically call p1() for each file
        const p1_cmd = b.addSystemCommand(&.{ "zig", "run", full_path, "-I", "src/myfolder", "-O", @tagName(optimize) });

        const p1_step = b.step(try std.fmt.allocPrint(b.allocator, "p1-{s}", .{std.fs.path.stem(entry.path)}), try std.fmt.allocPrint(b.allocator, "Run p1() in {s}", .{entry.path}));
        p1_step.dependOn(&p1_cmd.step);

        b.default_step.dependOn(p1_step);

        std.debug.print("-----------\n", .{});
    }
}
