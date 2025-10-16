<aside class="sidebar" aria-label="Main navigation">
    <nav>
        <a href="/" class="nav-link">Data Management</a>
        <a href="/stfn" class="nav-link">STFN</a>
        <a href="/mcda" class="nav-link">MCDA Analysis</a>
    </nav>
</aside>

<style>
    /* Fixed left sidebar layout */
    .sidebar {
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: 220px;
        background-color: #2c76b0;
        border-right: 1px solid #ccc;
        padding: 1rem;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        z-index: 1000;
    }

    nav {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .nav-link {
        text-decoration: none;
        color: #fff;
        font-weight: 600;
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        transition: background-color 0.15s ease;
    }

    .nav-link:hover,
    .nav-link:focus {
        background: rgba(255,255,255,0.08);
        text-decoration: none;
        outline: none;
    }

    /* Responsive: collapse to top horizontal bar on small screens */
    @media (max-width: 700px) {
        .sidebar {
            position: static;
            width: 100%;
            height: auto;
            border-right: none;
            border-bottom: 1px solid #ccc;
            flex-direction: row;
            align-items: center;
            padding: 0.5rem 0.75rem;
        }

        nav {
            flex-direction: row;
            gap: 1rem;
            width: 100%;
            justify-content: space-around;
        }

        .nav-link {
            padding: 0.5rem 0.6rem;
        }
    }
</style>
