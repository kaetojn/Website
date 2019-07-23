<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, WordPress Language, and ABSPATH. You can find more information
 * by visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('WP_CACHE', true); //Added by WP-Cache Manager
define( 'WPCACHEHOME', '/home3/realty/public_html/wp-content/plugins/wp-super-cache/' ); //Added by WP-Cache Manager
define('DB_NAME', 'realty_wrdp1');

/** MySQL database username */
define('DB_USER', 'realty_wrdp1');

/** MySQL database password */
define('DB_PASSWORD', 'aigeyr7wla0pFmTn');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

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
define('AUTH_KEY',         'Sh)x^@e:ZA\`W$@m(zIoP?3S<cvEX422blATf\`w(ffK$la)DEax==LapN35i32sRC29');
define('SECURE_AUTH_KEY',  '');
define('LOGGED_IN_KEY',    'kZ5x5?ftv_oD5>pKkwa=XuSvCGID@~:rgp$3mQ>\`Sn_Wos(/<98^(H\`7H6Cw>XWoV4r^pd');
define('NONCE_KEY',        'DhCB*6\`OgW3rVHQXN5BC\`2XkBhqK@?0D<(kCz#6~U-<P?0O?6Y<r;MihYAJKY)c~|\`(ms\`2Uj7F');
define('AUTH_SALT',        'tgDtF0!#H>TRIEe!V\`q6h!od!|)TIG(ft:EEZh5QIEqxKLgE:KeJ/V1c<\`b3(>jMl');
define('SECURE_AUTH_SALT', '1AF?0i>_sB)V^K<bpMrFXanx8Z>g@(;n0T8MC5KmYRCfbw|m8wkW;BR:$YRb=|d<');
define('LOGGED_IN_SALT',   '_:y;G1jkr4/i5ot;#N4=<uCiLhjD5J#Dy<pAevOjH=F=GoTIx=tktLez7#uo:3');
define('NONCE_SALT',       'r3T8uN:f/s1=^=CTXD0xGCkv7QhZTPh9Kq~SRK\`;l1b<nrXYw33s(J^cj6yvq!y)EY^<#-~Yveh');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * WordPress Localized Language, defaults to English.
 *
 * Change this to localize WordPress. A corresponding MO file for the chosen
 * language must be installed to wp-content/languages. For example, install
 * de_DE.mo to wp-content/languages and set WPLANG to 'de_DE' to enable German
 * language support.
 */
define('WPLANG', '');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
