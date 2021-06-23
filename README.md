<!-- README TEMPLATE FROM https://github.com/othneildrew/Best-README-Template -->
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/youstrollin/linux_automation">
    <img src="images/tux-python.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Linux automation stuff</h3>

  <p align="center">
    Misc scripts in Python for Linux automation.
    <br />
    <a href="https://www.linkedin.com/in/eduardo-amma-5b8a9831">LinkedIn</a>
    ·
    <a href="mailto:eduardoamma@gmail.com">Email</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <p><a>Completed</a>
      <ul>
        <li><a>Nothing here yet :(</a></li>
      </ul>
    </li>
    <li>
      <a href="#in-progress">In progress</a>
      <ul>
        <li>>asm_creation</li>
        <li>filesystem_full</li>
      </ul>
    </li>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

I suck at programming - if I don't have something useful, really useful, that requires it I simply can't do it. So, I started scripting some simple Linux stuff that I can use in my daily work and will scale it to include more complex and more ambitious features, hopefully it will improve my coding skills...Or at least entertain me because COVID sucks.

Most things that are not included in the Python code will probably be done with Ansible, if the playbook is not here then I either forgot or haven't worked on that yet.

## In Progress

### ASM disks creation (asm_creation)

This script is to automate the creation of ASM disks for Oracle RAC, in Virtual Machines or Physical servers, includes rescanning of LUNs, multipath configuration and GPT partitioning.

### Filesystem Full (filesystem_full)

This script is meant to evaluate and fix any reported "filesystem" full issues, includes validation of the filesystem, inode status check, will also remediate by removing files based on user input conditions (size, last modified, ownership, etc.) and/or performing online resizing if using LVM. Report only mode will also be available.