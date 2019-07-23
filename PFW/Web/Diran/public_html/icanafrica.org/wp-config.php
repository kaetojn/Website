<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'realty_wrdp2');

/** MySQL database username */
define('DB_USER', 'realty_wrdp2');

/** MySQL database password */
define('DB_PASSWORD', 'm4pxqM7fzHTg0z');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'N>$7Tr8<***RzHNo6Ou28:DRhzo-Xbq@wo)ffyi2A|rh$Ae^G-WEF1TIyH!a>OG');
define('SECURE_AUTH_KEY',  '*:b_ppN|/_$@g|C@6C1mC*Ezk!-wCQ8jlWgMv^t2^qc^eIm)ME8$;Ok6H<m(Jwe8-jiW');
define('LOGGED_IN_KEY',    'l^:|MIqr)r9dvcg<iwgiCL-t^IAryT1WJmF93>eTn\`X<EFGPj>^*r9UscT6#M^9;e!eyzMnQ4P!vh0BmV!');
define('NONCE_KEY',        ';k5iqX^3At$c@i;hsQW\`s@:COC#z1:nf:EyQSV;QMW@>G5_(h1:k^l-GmlP:u5KI\`?SsrZE');
define('AUTH_SALT',        '2CxSfLg0Epbg71=EQ5Al>^J4?;<hWJI~MMvJ!LzLAOfgHut(7GO9(<FqhiERZEQ*JtXmPLWD');
define('SECURE_AUTH_SALT', ';L5|ESyXSnl0<Yk:ap:ziVQ)YtwztpwP?ea?$s;08YbHs|?!vIobcvNajcRWPFAw');
define('LOGGED_IN_SALT',   '!m$~EnX-q~;h@0EyAaGOmov/JXt!7jIxTp~sVE_R;|cv6?6vywTVjcvXA=C\`=^E8_');
define('NONCE_SALT',       'y\`dRY8TM3BI-3A3x^~T8qJesjb(t?4=zPeML5jI1k|ELK9_|iClZ|b_01mZwR6E/m)pm6_lU:I=G');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
