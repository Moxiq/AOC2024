const std = @import("std");
const Builder = std.build.Builder;
const Step = std.build.Step;

pub fn build(b: *std.Build) !void {
    // Default target and optimize mode
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{ .preferred_optimize_mode = .Debug });

    // Create a module for io.zig that can be shared across executables
    const io_module = b.addModule("io", .{
        .root_source_file = b.path("src/io.zig"),
    });

    var src_dir = try std.fs.cwd().openDir(b.path("src").getPath(b), .{ .iterate = true });
    defer src_dir.close();

    // Create a step to run all executables
    const run_all_step = b.step("run-all", "Run all day executables");

    var dir_iterator = src_dir.iterate();
    while (try dir_iterator.next()) |entry| {
        // Check if the entry is a directory and starts with "day"
        if (entry.kind == .directory and std.mem.startsWith(u8, entry.name, "day")) {
            const day_path = b.fmt("src/{s}", .{entry.name});
            const main_path = b.fmt("{s}/main.zig", .{day_path});

            // Check if main.zig exists in the day directory
            src_dir.access(b.fmt("{s}/main.zig", .{entry.name}), .{}) catch continue;

            // Create executable
            const exe = b.addExecutable(.{
                .name = entry.name,
                .root_source_file = b.path(main_path),
                .target = target,
                .optimize = optimize,
            });

            // Add the io module to the executable
            exe.root_module.addImport("io", io_module);

            b.installArtifact(exe);

            // Create a run step for this executable
            const run_exe = b.addRunArtifact(exe);

            // Add to run-all step
            run_all_step.dependOn(&run_exe.step);
        }
    }
}
