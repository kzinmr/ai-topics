---
title: "How to build and publish multi-platform Rust binaries via Github actions"
url: "https://rakhim.exotext.com/how-to-build-and-publish-multi-platform-rust-binaries"
fetched_at: 2026-04-28T07:02:00.783677+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# How to build and publish multi-platform Rust binaries via Github actions

Source: https://rakhim.exotext.com/how-to-build-and-publish-multi-platform-rust-binaries

While developing
Textpod
(a simple note-taking app written in Rust), I needed to automate building and publishing on Github. This article (or the corresponding
set of YAML-files
) describes the setup which performs the following:
Build binaries for Windows and Linux
Build binaries for x86 Macs (Intel) and ARM Macs (arm64, M-chip)
Add the files to the latest Github release, along with checksums
Publish to crates.io
Build a lean Docker image for amd64 and arm64 platforms
Publish Docker images to Docker Hub
First, the trigger for these jobs is a release:
on:
  release:
    types:
    - created
The binaries for Linux and Windows can be built in the same Linux environment, using specific rustup targets:
jobs:
  linux_windows:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout the repository
      uses: actions/checkout@v2

    - name: Install Linux and Windows Cross Compilers
      run: sudo apt-get install --yes --no-install-recommends musl-tools gcc-mingw-w64-x86-64-win32

    - name: Install rustup targets
      run: rustup target add x86_64-unknown-linux-musl x86_64-pc-windows-gnu

    - name: Build the executable
      run: cargo build --release --target x86_64-unknown-linux-musl --target x86_64-pc-windows-gnu

    - name: Tar x86_64 binary
      run: tar -czvf textpod-gnu-linux-x86_64.tar.gz -C target/x86_64-unknown-linux-musl/release textpod

    - name: Zip windows binary
      run: zip -j textpod-windows.zip target/x86_64-pc-windows-gnu/release/textpod.exe

    - name: Generate SHA256 checksums
      run: |
        shasum -a 256 textpod-gnu-linux-x86_64.tar.gz > textpod-gnu-linux-x86_64.tar.gz.sha256
        shasum -a 256 textpod-windows.zip > textpod-windows.zip.sha256

    - name: Upload release binaries
      uses: alexellis/upload-assets@0.4.0
      env:
        GITHUB_TOKEN: ${{ github.token }}
      with:
        asset_paths: '["textpod-gnu-linux-x86_64.tar.gz", "textpod-windows.zip", "textpod-gnu-linux-x86_64.tar.gz.sha256", "textpod-windows.zip.sha256"]'
Step 4 (
cargo build
) produces two binary files. Next two steps archive them into tar.gz and .zip, respectively. Then checksums are calculated and saved into text files. The last step uses a
alexellis/upload-assets@0.4.0
action to attach all 4 files to the latest release.
${{ github.token }}
is an automatic variable, you don't have to create it manually anywhere.
Building for macOS is similar, but the job should run on a different platform (
runs-on: macos-latest
), and we want to have 2 targets: x86 and ARM (i.e. for Intel-based macs and newer ARM-based macs):
rustup target add x86_64-apple-darwin aarch64-apple-darwin
cargo build --release --target=x86_64-apple-darwin --target=aarch64-apple-darwin
To publish to crates.io, we use the
katyo/publish-crates@v2
action:
crates:
    runs-on: ubuntu-latest
    needs: [linux_windows, macos]
    steps:
    - uses: actions/checkout@v3
    - uses: actions-rs/toolchain@v1
      with:
        toolchain: stable
        override: true
    - uses: katyo/publish-crates@v2
      with:
        registry-token: ${{ secrets.CARGO_REGISTRY_TOKEN }}
The dependency
needs: [linux_windows, macos]
ensures that this step does not run unless builds for all OS platforms succeeded. You need to create an API token at
https://crates.io/settings/tokens
add it as the
CARGO_REGISTRY_TOKEN
variable to your github secrets.
The last step is to build a Docker image and publish it to Dockerhub:
docker:
    runs-on: ubuntu-latest
    needs: crates
    steps:
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v3
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      -
        name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        uses: docker/build-push-action@v6
        with:
          platforms: linux/amd64,linux/arm64
          push: true
          tags: freetonik/textpod:latest
Using the
docker/build-push-action@v6
, we produce amd64 and arm64 images. Again, you need to store
DOCKERHUB_USERNAME
and
DOCKERHUB_TOKEN
as secrets. Note that this step may take a lot of time (often 20-40 minutes).
As a result, when I create a new release on Github, a normal release page is created which only contains standard links to the source code. A pipeline starts in the background, and a few minutes later the release page gets populated with new files (
example
).
For Docker, we're using
rust:alpine
base image (see
Dockerfile
), which results in images roughly 10 MB in size (see
Docker hub
).
That's it! 🦀
P.S. Since the contents of files in the repo may change over time, here is the
permanent link to the
.workflows
directory
at the point in time when this article was published.
