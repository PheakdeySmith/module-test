import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
    plugins: [
        laravel({
            input: [
                'resources/css/app.css',
                'resources/js/app.js',
                // Admin module entries for dev server
                'Modules/Admin/resources/assets/sass/app.scss',
                'Modules/Admin/resources/assets/js/app.js',
            ],
            refresh: true,
        }),
        tailwindcss(),
    ],
    server: {
        watch: {
            ignored: ['**/storage/framework/views/**'],
        },
        fs: {
            // Allow serving files from Modules directory in dev
            allow: ['.', 'Modules']
        }
    },
});
