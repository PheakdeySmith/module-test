<?php

use Illuminate\Support\Facades\Route;
use Modules\Admin\App\Http\Controllers\AdminController;

Route::get('admins/crm-dashboard', [AdminController::class, 'crmDashboard'])->name('admin.crm');
Route::get('admins/access-roles', [AdminController::class, 'accessRoles'])->name('admin.access-roles');
Route::get('admins/access-permission', [AdminController::class, 'accessPermission'])->name('admin.access-permission');
Route::get('admins/users', [AdminController::class, 'userList'])->name('admin.users.index');
Route::get('admins/users/account', [AdminController::class, 'userViewAccount'])->name('admin.users.account');
Route::get('admins/users/billing', [AdminController::class, 'userViewBilling'])->name('admin.users.billing');
Route::get('admins/users/connections', [AdminController::class, 'userViewConnections'])->name('admin.users.connections');
Route::get('admins/users/notifications', [AdminController::class, 'userViewNotifications'])->name('admin.users.notifications');
Route::get('admins/users/security', [AdminController::class, 'userViewSecurity'])->name('admin.users.security');
Route::get('admins/invoices', [AdminController::class, 'invoiceList'])->name('admin.invoices.index');
Route::get('admins/invoices/add', [AdminController::class, 'invoiceAdd'])->name('admin.invoices.add');
Route::get('admins/invoices/edit', [AdminController::class, 'invoiceEdit'])->name('admin.invoices.edit');
Route::get('admins/invoices/preview', [AdminController::class, 'invoicePreview'])->name('admin.invoices.preview');
Route::get('admins/invoices/print', [AdminController::class, 'invoicePrint'])->name('admin.invoices.print');
Route::resource('admins', AdminController::class)->names('admin');
